import json
from typing import Self
from RequestBroker import RequestObjectBase
from geminiObjects import *


class TextToVideoCheckRequest(RequestObjectBase):
    def __init__(self, name: str, resolver: "TextToVideoRequestObject"):
        self._resolver = resolver
        super().__init__("")
        self._path = CreateRawPath(name)
        self._method = "GET"
        self._header = {"Content-Type": "application/json"}

    def resolve(self, result: bytes) -> Self:
        return self._resolver.resolve(result)

    def error(self, error):
        return self._resolver.error(error)


class TextToVideoRequestObject(RequestObjectBase):
    def __init__(
        self,
        input: GeminiVideoInput,
        outputOp: moviefileinTOP,
        model: Model = Model.VEO_3_1_GENERATE_PREVIEW,
    ):
        data = input.render()
        data_string = json.dumps(data)
        super().__init__(data_string)

        self._output = outputOp

        self._path = CreatePath(model, Operation.PREDICT_LONG_RUNNING)
        self._method = "POST"
        self._header = {"Content-Type": "application/json"}

    def resolve(self, result: bytes) -> TextToVideoCheckRequest:
        text = result.decode("utf-8", errors="ignore")
        data = json.loads(text)

        print(text)

        if "done" not in data:
            return TextToVideoCheckRequest(data["name"], self)

        print(data["response"])
        filePath = data["response"]["generateVideoResponse"]["generatedSamples"][0][
            "video"
        ]["uri"]

        key = self._output.parent.geminiCOMP.fetch("gemini_apiKey")
        self._output.par.file = filePath + f"&key={key}"

    def error(self, error):
        if self._on_error_cb is not None:
            self._on_error_cb()
        return super().error(error)
