import json
import base64

from RequestBroker import RequestObjectBase
from geminiObjects import *


class ImageTextToTextRequestObject(RequestObjectBase):
    def __init__(self, input: GeminiInput, output: textDAT):
        data = input.render()
        data_string = json.dumps(data)
        super().__init__(data_string)

        self._output = output

        self._url = CreateEndpoint(
            Model.GEMINI_3_FLASH_PREVIEW, Operation.GENERATE_CONTENT
        )
        self._method = "POST"
        self._header = {"Content-Type": "application/json"}

    def resolve(self, result: bytes):
        text = result.decode("utf-8", errors="ignore")
        output = GeminiOutput.fromJson(text)
        output_text = ""

        for candidate in output.candidates:
            for part in candidate.content.parts:
                output_text = output_text + part.text + "\n"

        self._output.text = output_text
        self._output.store("metadata", output.usage_metadata.toDict())
        return None

    def error(self, error):
        if self._on_error_cb is not None:
            self._on_error_cb()
        return super().error(error)
