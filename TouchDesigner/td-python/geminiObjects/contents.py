from abc import ABC, abstractmethod
import json
import base64
from generationConfig import *


class GeminiContentPart(ABC):
    @abstractmethod
    def renderPart(self) -> dict:
        raise Exception("unimplemented")


class GeminiContentTextPart(GeminiContentPart):
    def __init__(self, text: str):
        self._text = text
        self._role = ""

    def renderPart(self) -> dict:
        part = {"text": self._text}
        return part


class GeminiContentImagePart(GeminiContentPart):
    def __init__(self, mime_type: str, image_bytes: bytes):
        self._mime_type = mime_type
        self._data = base64.b64encode(image_bytes).decode("utf-8")

    def renderPart(self) -> dict:
        return {"inline_data": {"mime_type": self._mime_type, "data": self._data}}


class ImageConfig:
    def __init__(self):
        # defaults
        self.aspect = GenerationAspectRatio.ASPECT_1_1
        self.image_size = GenerationImageSize.RESOLUTION_512

    def SetAspect(self, aspect: GenerationAspectRatio):
        self.aspect = aspect

    def SetImageSize(self, size: GenerationImageSize):
        self.image_size = size


class ThinkingConfig:
    def __init__(self):
        # defaults
        self.thinking_level = GenerationThinkingLevel.LOW

    def SetThinkingLevel(self, level: GenerationThinkingLevel):
        self.thinking_level = level


class SpeechConfig:
    def __init__(self):
        self.voiceName = TTSVoiceName.KORE

    def SetPrebuiltVoice(self, voice: TTSVoiceName):
        self.voiceName = voice


class GenerationConfig:
    def __init__(self):
        self._image_config = None
        self._thinking_config = None
        self._speech_config = None
        pass

    def AddThinkingConfig(self) -> ThinkingConfig:
        self._thinking_config = ThinkingConfig()
        return self._thinking_config

    def AddImageConfig(self) -> ImageConfig:
        self._image_config = ImageConfig()
        return self._image_config

    def AddSpeechConfig(self) -> SpeechConfig:
        self._speech_config = SpeechConfig()
        return self._speech_config

    def render(self) -> dict:
        config = {}
        if self._image_config is not None:
            # add image config
            config["imageConfig"] = {
                "aspectRatio": str(self._image_config.aspect),
                "imageSize": str(self._image_config.image_size),
            }

        if self._thinking_config is not None:
            # add thinking config
            config["thinkingConfig"] = {
                "thinkingLevel": str(self._thinking_config.thinking_level)
            }

        if self._speech_config is not None:
            # add thinking config
            config["speechConfig"] = {
                "voiceConfig": {
                    "prebuiltVoiceConfig": {
                        "voiceName": str(self._speech_config.voiceName)
                    }
                }
            }

        return config


class GeminiContent:
    def __init__(self, role: str):
        self._parts: list[GeminiContentPart] = []
        self._role = role

    def renderContents(self) -> dict:
        contentsData = [p.renderPart() for p in self._parts]
        content = {"role": self._role, "parts": contentsData}
        return content

    def addPart(self, part: GeminiContentPart):
        self._parts.append(part)

    def addTextPart(self, text: str):
        newPart = GeminiContentTextPart(text)
        self.addPart(newPart)

    def addImagePart(self, mime_type: str, image_bytes: bytes):
        newPart = GeminiContentImagePart(mime_type, image_bytes)
        self.addPart(newPart)


class GeminiInput:
    def __init__(self):
        self._contents: list[GeminiContent] = []
        self._generation_config: GenerationConfig = None

    def render(self) -> dict:
        contents = [c.renderContents() for c in self._contents]
        data = {"contents": contents}

        if self._generation_config is not None:
            data["generationConfig"] = self._generation_config.render()

        return data

    def addGenerationConfig(self) -> GenerationConfig:
        self._generation_config = GenerationConfig()
        return self._generation_config

    def addContent(self, content: list[GeminiContent]):
        self._contents.extend(content)
        return

    def addUserContent(self) -> GeminiContent:
        c = GeminiContent("user")
        self._contents.append(c)
        return c

    def addModelContent(self) -> GeminiContent:
        c = GeminiContent("model")
        self._contents.append(c)
        return c


class GeminiReferenceImage:
    def __init__(self, operator: TOP):
        image_bytes = operator.saveByteArray(".png")
        self._data = base64.b64encode(image_bytes).decode("utf-8")
        self._mimeType = "image/png"
        pass

    def render(self) -> dict:
        return {
            "image": {"inlineData": {"mimeType": self._mimeType, "data": self._data}},
            "referenceType": "asset",
        }


class GeminiFrameImage:
    def __init__(self, operator: TOP):
        image_bytes = operator.saveByteArray(".png")
        self._data = base64.b64encode(image_bytes).decode("utf-8")
        self._mimeType = "image/png"
        pass

    def render(self) -> dict:
        return {"mimeType": self._mimeType, "bytesBase64Encoded": self._data}


class GeminiPromptInstance:
    def __init__(self, prompt: str):
        self._prompt = prompt
        self._first_frame = None
        self._last_frame = None
        self._references: list[GeminiReferenceImage] = []
        pass

    def addReferenceImageFromOperator(self, operator: TOP):
        self._references.append(GeminiReferenceImage(operator))
        pass

    def addFirstFrame(self, operator: TOP):
        self._first_frame = GeminiFrameImage(operator)
        pass

    def addLastFrame(self, operator: TOP):
        self._last_frame = GeminiFrameImage(operator)
        pass

    def render(self) -> dict:

        data = {
            "prompt": self._prompt,
        }
        if self._first_frame is not None:
            data["image"] = self._first_frame.render()

        if self._last_frame is not None:
            data["lastFrame"] = self._last_frame.render()

        if len(self._references) > 0:
            data["referenceImages"] = [i.render() for i in self._references]

        return data


class GeminiVideoParameters:
    def __init__(self):
        self._aspect: VeoParameterAspectRatio = None
        self._resolution: VeoParameterResolution = None
        self._duration: VeoParameterDuration = None
        pass

    def render(self) -> dict:
        data = {}
        if self._aspect is not None:
            data["aspectRatio"] = self._aspect.value
        if self._resolution is not None:
            data["resolution"] = self._resolution.value
        if self._duration is not None:
            data["durationSeconds"] = int(self._duration.value)
        return data

    def setAspect(self, aspect: VeoParameterAspectRatio):
        self._aspect = aspect

    def setResolution(self, resolution: VeoParameterResolution):
        self._resolution = resolution

    def setDuration(self, duration: VeoParameterDuration):
        self._duration = duration


class GeminiVideoInput:
    def __init__(self):
        self._instances: list[GeminiPromptInstance] = []
        self._parameters: GeminiVideoParameters = None
        pass

    def addParameters(self) -> GeminiVideoParameters:
        params = GeminiVideoParameters()
        self._parameters = params
        return params

    def addPromptInstance(self, prompt: str) -> GeminiPromptInstance:
        instance = GeminiPromptInstance(prompt)
        self._instances.append(instance)
        return instance

    def render(self) -> dict:

        data = {"instances": [i.render() for i in self._instances]}
        if self._parameters is not None:
            data["parameters"] = self._parameters.render()
        return data


class GeminiOutputPart:
    def __init__(self, input: dict):

        self.text = None
        self.inline_data = None
        self.mime_type = None
        self.data = None

        if "text" in input:
            self.text = input["text"]

        if "inlineData" in input:
            self.inline_data = input["inlineData"]
            self.mime_type = input["inlineData"]["mimeType"]
            self.data = input["inlineData"]["data"]

        if "thoughtSignature" in input:
            self.thought_signature = input["thoughtSignature"]
        pass


class GeminiOutputContent:
    def __init__(self, input: dict):
        self.parts = [GeminiOutputPart(p) for p in input["parts"]]
        self.role = input["role"]
        pass


class GeminiCandidate:
    def __init__(self, input: dict):
        self.content = GeminiOutputContent(input["content"])
        self.finish_reason = input["finishReason"]
        self.index = input["index"]
        pass


class GeminiUsageMetadata:
    def __init__(self, input: dict):
        self._data = input
        self.prompt_token_count = input["promptTokenCount"]
        self.candidates_token_count = input["candidatesTokenCount"]
        self.total_token_count = input["totalTokenCount"]
        self.prompt_tokens_details = input["promptTokensDetails"]
        # self.thoughts_token_count = input['thoughtsTokenCount']
        pass

    def toDict(self) -> dict:
        return self._data


class GeminiOutput:
    def __init__(self, input: dict):
        self.model_version = input["modelVersion"]
        self.response_id = input["responseId"]
        self.usage_metadata = GeminiUsageMetadata(input["usageMetadata"])
        self.candidates = [GeminiCandidate(c) for c in input["candidates"]]
        pass

    @classmethod
    def fromJson(cls, json_str: str):
        data = json.loads(json_str)
        return cls(data)
