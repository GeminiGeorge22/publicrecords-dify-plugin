from __future__ import annotations

import re
from collections.abc import Generator
from typing import Any

import requests
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

APIFY_API = "https://api.apify.com/v2"
DATASET_ID_RE = re.compile(r"^[A-Za-z0-9]{8,32}$")


class GetDatasetItemsTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        token = (self.runtime.credentials or {}).get("apify_api_token")
        if not token or not str(token).strip():
            yield self.create_text_message(
                "An Apify API token is required. Add your own token in the plugin credentials."
            )
            return
        token = str(token).strip()

        dataset_id = str(tool_parameters.get("dataset_id") or "").strip()
        if not DATASET_ID_RE.fullmatch(dataset_id):
            yield self.create_text_message(
                "dataset_id must be an Apify dataset id (letters and digits only)."
            )
            return

        def as_int(value: Any, default: int, minimum: int, maximum: int) -> int:
            try:
                number = int(value)
            except (TypeError, ValueError):
                return default
            return max(minimum, min(maximum, number))

        limit = as_int(tool_parameters.get("limit"), 25, 1, 100)
        offset = as_int(tool_parameters.get("offset"), 0, 0, 100000)

        try:
            response = requests.get(
                f"{APIFY_API}/datasets/{dataset_id}/items",
                headers={
                    "Authorization": f"Bearer {token}",
                    "Accept": "application/json",
                },
                params={"limit": limit, "offset": offset, "clean": "true"},
                timeout=30,
            )
        except requests.RequestException:
            yield self.create_text_message("Could not reach the Apify API to read the dataset.")
            return

        if response.status_code in (401, 403):
            yield self.create_text_message(
                "The Apify API token was rejected. Check the token in the plugin credentials."
            )
            return
        if response.status_code == 404:
            yield self.create_text_message("That dataset was not found, or this token cannot read it.")
            return
        if not response.ok:
            yield self.create_text_message(
                f"Apify API returned HTTP {response.status_code} when reading the dataset."
            )
            return

        items = response.json() if response.content else []
        count = len(items) if isinstance(items, list) else 0
        yield self.create_text_message(f"Returned {count} item(s) from dataset {dataset_id}.")
        yield self.create_json_message(
            {
                "dataset_id": dataset_id,
                "limit": limit,
                "offset": offset,
                "item_count_returned": count,
                "items": items,
            }
        )
