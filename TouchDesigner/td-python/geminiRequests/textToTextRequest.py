import json
from RequestBroker import RequestObjectBase
from geminiObjects import *


class TextToTextRequestObject(RequestObjectBase):
    def __init__(self, input: GeminiInput, outputOp: textDAT, model: Model = Model.GEMINI_3_FLASH_PREVIEW):
        data = input.render()
        data_string = json.dumps(data)
        super().__init__(data_string)

        self._output = outputOp

        self._url = CreateEndpoint(
            model, Operation.GENERATE_CONTENT)
        self._method = "POST"
        self._header = {
            "Content-Type": "application/json"
        }

    def resolve(self, result: bytes):
        text = result.decode("utf-8", errors="ignore")
        output = GeminiOutput.fromJson(text)

        output_text = ""

        for candidate in output.candidates:
            for part in candidate.content.parts:
                output_text = output_text+part.text+"\n"

        self._output.text = output_text
        self._output.store("metadata",  output.usage_metadata.toDict())

    def error(self, error):
        return super().error(error)
