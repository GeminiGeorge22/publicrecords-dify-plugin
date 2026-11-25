from typing import Any

import requests
from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

APIFY_ME_URL = "https://api.apify.com/v2/users/me"


class PublicRecordsProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        token = (credentials or {}).get("apify_api_token")
        if not token or not str(token).strip():
            raise ToolProviderCredentialValidationError(
                "An Apify API token is required. Enter your own token from the Apify Console."
            )
        try:
            response = requests.get(
                APIFY_ME_URL,
                headers={"Authorization": f"Bearer {str(token).strip()}"},
                timeout=20,
            )
        except requests.RequestException as exc:
            raise ToolProviderCredentialValidationError(
                "Could not reach the Apify API to validate the token."
            ) from exc
        if response.status_code in (401, 403):
            raise ToolProviderCredentialValidationError(
                "The Apify API token was rejected. Check that you pasted your own token."
            )
        if not response.ok:
            raise ToolProviderCredentialValidationError(
                f"Apify API returned HTTP {response.status_code} while validating the token."
            )
