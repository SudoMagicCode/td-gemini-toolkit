import json
from typing import Self
from RequestBroker import RequestObjectBase
from geminiObjects import *


class VertexTextToVideoCheckRequest(RequestObjectBase):
    def __init__(self, path: str, name: str, resolver: "TextToVideoRequestObject"):
        self._resolver = resolver

        data = {
            "operationName": name,
        }

        data_string = json.dumps(data)

        super().__init__(data_string)
        self._path = path
        self._method = "POST"
        self._header = {"Content-Type": "application/json"}

    def resolve(self, result: bytes) -> Self:
        return self._resolver.resolve(result)

    def error(self, error):
        return self._resolver.error(error)


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
        model: GeminiModel = StudioModels.VEO_3_1_GENERATE_PREVIEW,
    ):
        data = input.render()
        data_string = json.dumps(data)
        super().__init__(data_string)

        self._output = outputOp
        self._model = model
        self._path = CreatePath(model.model, Operation.PREDICT_LONG_RUNNING)
        self._method = "POST"
        self._header = {"Content-Type": "application/json"}

    def resolve(self, result: bytes) -> TextToVideoCheckRequest:
        text = result.decode("utf-8", errors="ignore")
        data = json.loads(text)

        if "done" not in data:
            name: str = data["name"]
            if name.find("/google") != -1:
                checkPath = CreatePath(
                    self._model.model, Operation.FETCH_PREDICT_OPERATION
                )
                return VertexTextToVideoCheckRequest(checkPath, name, self)
            #     # the path that comes back from the model is too long for the url parser in the request broker
            #     # so we split it at an appropraite place
            #     parts = name.split("/google/")
            #     return TextToVideoCheckRequest(parts[1], self)
            return TextToVideoCheckRequest(name, self)

        if "@type" in data["response"]:
            # this is a vertex response
            base64Video = data["response"]["videos"][0]["bytesBase64Encoded"]
            video_bytes = base64.b64decode(base64Video)
            try:
                self._output.parent.geminiCOMP.vfs["temp.mp4"].destroy()
            except:
                pass
            self._output.parent.geminiCOMP.vfs.addByteArray(video_bytes, "temp.mp4")

            path = self._output.parent.geminiCOMP.path
            self._output.par.file = f"vfs:{path}:temp.mp4"
            self._output.par.reloadpulse.pulse()
            return

        filePath = data["response"]["generateVideoResponse"]["generatedSamples"][0][
            "video"
        ]["uri"]

        key = parent.geminiCOMP.mod.apiKeyActions.resolveEndpointInfo().get("apiKey")
        self._output.par.file = filePath + f"&key={key}"

    def error(self, error):
        if self._on_error_cb is not None:
            self._on_error_cb()
        return super().error(error)
