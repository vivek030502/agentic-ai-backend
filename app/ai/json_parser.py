import json
import re
from typing import Type

from pydantic import BaseModel
from pydantic import ValidationError

from app.ai.exceptions import AIResponseParseException
from app.config.logger import app_logger


class JsonResponseParser:
    """
    Parses LLM responses into Pydantic models.

    Handles:

    - ```json ... ```
    - ``` ... ```
    - surrounding whitespace

    Then validates against a Pydantic model.
    """

    def parse(
        self,
        response: str,
        model: Type[BaseModel],
    ) -> BaseModel:

        cleaned = self._clean(response)

        try:

            data = json.loads(cleaned)

        except Exception as ex:

            app_logger.error("========== INVALID JSON ==========")
            app_logger.error(cleaned)
            app_logger.error("==================================")

            raise AIResponseParseException(
                "LLM returned invalid JSON."
            ) from ex

        try:

            return model.model_validate(data)

        except ValidationError as ex:

            raise AIResponseParseException(
                str(ex)
            ) from ex

    def _clean(
        self,
        text: str,
    ) -> str:

        text = text.strip()

        if text.startswith("```json"):

            text = text[7:]

        elif text.startswith("```"):

            text = text[3:]

        if text.endswith("```"):

            text = text[:-3]

        return text.strip()