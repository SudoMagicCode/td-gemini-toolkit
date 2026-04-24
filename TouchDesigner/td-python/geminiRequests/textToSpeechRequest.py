import json
import base64

from RequestBroker import RequestObjectBase
from geminiObjects import *

import wave
import io


def save_wav_file(base64_audio_string) -> bytes:
    # 1. Decode the base64 string into raw PCM bytes
    pcm_bytes = base64.b64decode(base64_audio_string)

    # 2. Set the audio parameters required by the Gemini API output
    channels = 1  # Mono audio
    sample_width = 2  # 16-bit audio (2 bytes per sample)
    frame_rate = 24000  # 24 kHz sample rate

    # 2. Create an in-memory bytes buffer
    wav_io = io.BytesIO()

    # 3. Write the WAV header and PCM data into the buffer instead of a file
    with wave.open(wav_io, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(24000)
        wf.writeframes(pcm_bytes)

    # 4. Extract the final WAV-formatted bytes
    wav_bytes = wav_io.getvalue()
    return wav_bytes


class TextToSpeechRequest(RequestObjectBase):
    def __init__(
        self,
        input: GeminiInput,
        output: audiofileinCHOP,
        model: GeminiModel = Models.GEMINI_3_1_FLASH_PREVIEW_TTS,
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
        output = GeminiOutput.fromJson(text)

        for candidate in output.candidates:
            for part in candidate.content.parts:
                if part.data is not None:
                    if len(part.data) > 0:
                        audio_bytes = save_wav_file(part.data)
                        try:
                            self._output.parent.geminiCOMP.vfs["temp.wav"].destroy()
                        except Exception:
                            pass
                        print("adding vfs")
                        self._output.parent.geminiCOMP.vfs.addByteArray(
                            audio_bytes, "temp.wav"
                        )
        path = self._output.parent.geminiCOMP.path

        self._output.parent.geminiCOMP.par.File.expr = 'f"vfs:{me.path}:temp.wav"'
        self._output.parent.geminiCOMP.par.Reloadpulse.pulse()
        return None

    def error(self, error):
        if self._on_error_cb is not None:
            self._on_error_cb()
        return super().error(error)
