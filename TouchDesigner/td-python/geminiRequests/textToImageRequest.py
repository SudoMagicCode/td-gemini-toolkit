import json
import base64

from RequestBroker import RequestObjectBase
from geminiObjects import *


class TextToImageRequestObject(RequestObjectBase):
    def __init__(
        self,
        input: GeminiInput,
        output: scriptTOP,
        model: Model = Models.GEMINI_3_1_FLASH_IMAGE_PREVIEW,
    ):
        data = input.render()
        data_string = json.dumps(data)
        super().__init__(data_string)

        self._output = output

        self._path = CreatePath(model, Operation.GENERATE_CONTENT)
        self._method = "POST"
        self._header = {"Content-Type": "application/json"}

    def resolve(self, result: bytes):
        text = result.decode("utf-8", errors="ignore")
        # print(text)
        output = GeminiOutput.fromJson(text)
        for candidate in output.candidates:
            for part in candidate.content.parts:
                # print(part)
                if len(part.data) > 0:
                    img_bytes = base64.b64decode(part.data)
                    self._output.store("image_data", img_bytes)
                    self._output.store("mime", ".jpg")

        self._output.store("metadata", output.usage_metadata.toDict())
        return None

    def error(self, error):
        if self._on_error_cb is not None:
            self._on_error_cb()
        return super().error(error)
