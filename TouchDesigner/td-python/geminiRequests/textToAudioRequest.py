import json
import base64

from RequestBroker import RequestObjectBase
from geminiObjects import *


class TextToAudioRequest(RequestObjectBase):
    def __init__(
        self,
        input: GeminiInput,
        output: audiofileinCHOP,
        model: Model = Model.LYRIA_3_CLIP_PREVIEW,
    ):
        data = input.render()
        data_string = json.dumps(data)
        super().__init__(data_string)

        self._output = output

        self._url = CreateEndpoint(model, Operation.GENERATE_CONTENT)
        self._method = "POST"
        self._header = {"Content-Type": "application/json"}

    def resolve(self, result: bytes):
        text = result.decode("utf-8", errors="ignore")
        output = GeminiOutput.fromJson(text)

        for candidate in output.candidates:
            for part in candidate.content.parts:
                if part.data is not None:
                    if len(part.data) > 0:
                        audio_bytes = base64.b64decode(part.data)
                        try:
                            self._output.parent.geminiCOMP.vfs["temp.mp3"].destroy()
                        except:
                            pass
                        self._output.parent.geminiCOMP.vfs.addByteArray(
                            audio_bytes, "temp.mp3"
                        )
        path = self._output.parent.geminiCOMP.path

        self._output.parent.geminiCOMP.par.File.expr = 'f"vfs:{me.path}:temp.mp3"'
        self._output.parent.geminiCOMP.par.Reloadpulse.pulse()

        return None

    def error(self, error):
        if self._on_error_cb is not None:
            self._on_error_cb()
        return super().error(error)
