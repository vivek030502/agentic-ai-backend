# import base64
# import json
# import re

# from app.code_generation.models import (
#     CodeGenerationResponse,
#     GeneratedFile,
# )


# class CodeParser:

#     def parse(
#         self,
#         response: str,
#     ) -> CodeGenerationResponse:

#         response = response.strip()

#         match = re.search(
#             r"```(?:json)?\s*(.*?)\s*```",
#             response,
#             re.DOTALL,
#         )

#         if match:
#             response = match.group(1)

#         data = json.loads(response)

#         files = []

#         for item in data["files"]:

#             content = base64.b64decode(
#                 item["content_base64"]
#             ).decode("utf-8")

#             files.append(
#                 GeneratedFile(
#                     file_path=item["file_path"],
#                     language=item["language"],
#                     content=content,
#                 )
#             )

#         return CodeGenerationResponse(
#             files=files
#         )



from app.ai.json_parser import JsonResponseParser

from app.code_generation.models import (
    CodeGenerationResponse,
)


class CodeParser:

    def __init__(self):

        self.parser = JsonResponseParser()

    def parse(
        self,
        response: str,
    ) -> CodeGenerationResponse:

        return self.parser.parse(
            response,
            CodeGenerationResponse,
        )