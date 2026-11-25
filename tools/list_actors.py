from collections.abc import Generator
from typing import Any

from actors import ACTORS
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage


class ListActorsTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage, None, None]:
        payload = {"actors": ACTORS, "count": len(ACTORS)}
        lines = [f"{a['id']}: {a['one_line']} ({a['store_url']})" for a in ACTORS]
        yield self.create_text_message("\n".join(lines))
        yield self.create_json_message(payload)
