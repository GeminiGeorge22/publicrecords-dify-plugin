from __future__ import annotations

import json
from collections.abc import Generator
from typing import Any

import requests
from actors import resolve_actor_id
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

APIFY_API = "https://api.apify.com/v2"


def _auth_headers(token: str) -> dict[str, str]:
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def _parse_input(raw: Any) -> dict[str, Any] | list[Any] | None:
    if raw is None or raw == "":
        return {}
    if isinstance(raw, (dict, list)):
        return raw
    if not isinstance(raw, str):
        return None
    text = raw.strip()
    if not text:
        return {}
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return None
    if not isinstance(data, (dict, list)):
        return None
    return data


def _as_int(value: Any, default: int, minimum: int, maximum: int) -> int:
    try:
        number = int(value)
    except (TypeError, ValueError):
        return default
    return max(minimum, min(maximum, number))


class RunActorTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        token = (self.runtime.credentials or {}).get("apify_api_token")
        if not token or not str(token).strip():
            yield self.create_text_message(
                "An Apify API token is required. Add your own token in the plugin credentials."
            )
            return
        token = str(token).strip()

        actor_id = resolve_actor_id(str(tool_parameters.get("actor") or ""))
        if not actor_id:
            yield self.create_text_message(
                "That Actor is not on the Public Records allowlist. Call list_actors for valid ids."
            )
            return

        actor_input = _parse_input(tool_parameters.get("input_json"))
        if actor_input is None:
            yield self.create_text_message("input_json must be a JSON object (or a JSON array).")
            return

        wait = _as_int(tool_parameters.get("wait_for_finish"), 90, 0, 150)
        max_items = _as_int(tool_parameters.get("max_items"), 25, 1, 100)
        actor_path = actor_id.replace("/", "~")
        url = f"{APIFY_API}/acts/{actor_path}/runs"
        timeout = max(30, wait + 30)

        try:
            response = requests.post(
                url,
                headers=_auth_headers(token),
                params={"waitForFinish": wait},
                json=actor_input,
                timeout=timeout,
            )
        except requests.RequestException:
            yield self.create_text_message("Could not reach the Apify API to start the run.")
            return

        if response.status_code in (401, 403):
            yield self.create_text_message(
                "The Apify API token was rejected. Check the token in the plugin credentials."
            )
            return
        if not response.ok:
            yield self.create_text_message(
                f"Apify API returned HTTP {response.status_code} when starting {actor_id}."
            )
            return

        body = response.json() if response.content else {}
        data = body.get("data") or body
        run_id = data.get("id")
        status = data.get("status")
        dataset_id = data.get("defaultDatasetId")
        result: dict[str, Any] = {
            "actor": actor_id,
            "run_id": run_id,
            "status": status,
            "default_dataset_id": dataset_id,
            "started_at": data.get("startedAt"),
            "finished_at": data.get("finishedAt"),
            "console_url": f"https://console.apify.com/actors/{actor_path}/runs/{run_id}" if run_id else None,
        }

        if status == "SUCCEEDED" and dataset_id:
            try:
                items_resp = requests.get(
                    f"{APIFY_API}/datasets/{dataset_id}/items",
                    headers=_auth_headers(token),
                    params={"limit": max_items, "clean": "true"},
                    timeout=30,
                )
                if items_resp.ok:
                    items = items_resp.json()
                    result["item_count_returned"] = len(items) if isinstance(items, list) else 0
                    result["items"] = items
            except requests.RequestException:
                result["items_error"] = "The run finished, but dataset items could not be fetched."

        yield self.create_text_message(
            f"{actor_id} run {run_id or '(unknown)'} status {status or '(unknown)'}"
            + (f", dataset {dataset_id}" if dataset_id else "")
        )
        yield self.create_json_message(result)
