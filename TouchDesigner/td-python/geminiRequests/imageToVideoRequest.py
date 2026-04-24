import json
from typing import Self
from RequestBroker import RequestObjectBase
from geminiObjects import *


class ImageToVideoCheckRequest(RequestObjectBase):
    def __init__(self, name: str, resolver: "ImageToVideoRequestObject"):
        self._resolver = resolver
        super().__init__("")
        self._path = CreateRawPath(name)
        self._method = "GET"
        self._header = {"Content-Type": "application/json"}

    def resolve(self, result: bytes) -> Self:
        return self._resolver.resolve(result)

    def error(self, error):
        return self._resolver.error(error)


class ImageToVideoRequestObject(RequestObjectBase):
    def __init__(
        self,
        input: GeminiVideoInput,
        outputOp: moviefileinTOP,
        model: GeminiModel = StudioModels.VEO_3_1_GENERATE_PREVIEW,
    ):
        data = input.render()
        data_string = json.dumps(data)
        super().__init__(data_string)

        self._output = outputOp

        self._path = CreatePath(model.model, Operation.PREDICT_LONG_RUNNING)
        self._method = "POST"
        self._header = {"Content-Type": "application/json"}

    def resolve(self, result: bytes) -> ImageToVideoCheckRequest:
        text = result.decode("utf-8", errors="ignore")
        data = json.loads(text)

        if "done" not in data:
            name: str = data["name"]
            # the path that comes back from the model is too long for the url parser in the request broker
            # so we split it at an appropraite place
            parts = name.split("/google/")
            return ImageToVideoCheckRequest(parts[1], self)

        filePath = data["response"]["generateVideoResponse"]["generatedSamples"][0][
            "video"
        ]["uri"]

        # resolve apiKey from geminiCOMP
        key = parent.geminiCOMP.mod.apiKeyActions.resolveEndpointInfo().get("apiKey")
        self._output.par.file = filePath + f"&key={key}"

    def error(self, error):
        if self._on_error_cb is not None:
            self._on_error_cb()
        return super().error(error)
