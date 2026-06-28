from typing import Any

import requests

from app.config.logger import app_logger


class BaseHttpClient:
    """
    Base HTTP client used by all external integrations.

    Provides common functionality such as:
    - Authentication headers
    - Timeouts
    - Logging
    - Error handling
    """

    DEFAULT_TIMEOUT = 30

    def __init__(
        self,
        base_url: str,
        headers: dict[str, str] | None = None,
    ):
        self.base_url = base_url.rstrip("/")
        self.headers = headers or {}

    def get(
        self,
        endpoint: str,
        params: dict[str, Any] | None = None,
    ) -> requests.Response:
        """
        Execute an HTTP GET request.
        """

        url = f"{self.base_url}{endpoint}"

        app_logger.info(f"GET {url}")

        response = requests.get(
            url,
            headers=self.headers,
            params=params,
            timeout=self.DEFAULT_TIMEOUT,
        )

        app_logger.info(f"Response Status : {response.status_code}")

        if not response.ok:
            app_logger.error(f"Response Body : {response.text}")

        response.raise_for_status()

        return response

    def post(
        self,
        endpoint: str,
        json_data: dict[str, Any],
    ) -> requests.Response:
        """
        Execute an HTTP POST request.
        """

        url = f"{self.base_url}{endpoint}"

        app_logger.info(f"POST {url}")
        app_logger.debug(f"Request Body : {json_data}")

        response = requests.post(
            url,
            headers=self.headers,
            json=json_data,
            timeout=self.DEFAULT_TIMEOUT,
        )

        app_logger.info(f"Response Status : {response.status_code}")

        if not response.ok:
            app_logger.error(f"Response Body : {response.text}")

        response.raise_for_status()

        return response