from enum import Enum
from dataclasses import dataclass
import geminiTerminalLogs
import geminiObjects


class geminiOPType(Enum):
    G_TXT_TO_TXT = "gTxtToTxt"
    G_TXT_CHAT = "gTxtChat"
    G_IMG_TO_TXT = "gImgToTxt"
    G_TXT_TO_IMG = "gTxtToImg"
    G_IMG_TO_IMG = "gImgToImg"
    G_TXT_TO_VID = "gTxtToVid"
    G_IMG_TO_VID = "gImgToVid"
    G_AUDIO_TO_TXT = "gAudioToTxt"
    G_TXT_TO_AUDIO = "gTxtToAudio"
    G_TXT_TO_SPEECH = "gTxtToSpeech"


class geminiReturnData(Enum):
    TEXT = "text"
    VIDEO = "video"
    AUDIO = "audio"
    IMAGE = "image"


@dataclass
class geminiOP:
    name: str
    opType: geminiOPType
    returnData: str
    studioEnumPar: str
    vertexEnumPar: str

    def __repr__(self) -> str:
        return self.name


gTxtToTxt = geminiOP(
    name="Gemini Text to Text",
    opType=geminiOPType.G_TXT_TO_TXT,
    returnData=geminiReturnData.TEXT,
    studioEnumPar="me.mod.smOpUtils.menuPars.fromEnumPar(me.mod.enumPars.StudioTextModels)",
    vertexEnumPar="me.mod.smOpUtils.menuPars.fromEnumPar(me.mod.enumPars.VertexTextModels)",
)
gTxtChat = geminiOP(
    name="Gemini Text Chat",
    opType=geminiOPType.G_TXT_CHAT,
    returnData=geminiReturnData.TEXT,
    studioEnumPar=geminiObjects.StudioModels.DEPRECATED_GEMINI_3_FLASH_PREVIEW.name,
    vertexEnumPar=geminiObjects.VertexModels.DEPRECATED_GEMINI_3_FLASH_PREVIEW.name,
)
gImgToTxt = geminiOP(
    name="Gemini Image to Text",
    opType=geminiOPType.G_IMG_TO_TXT,
    returnData=geminiReturnData.TEXT,
    studioEnumPar=geminiObjects.StudioModels.DEPRECATED_GEMINI_3_FLASH_PREVIEW.name,
    vertexEnumPar=geminiObjects.VertexModels.DEPRECATED_GEMINI_3_FLASH_PREVIEW.name,
)
gTxtToImg = geminiOP(
    name="Gemini Text to Image",
    opType=geminiOPType.G_TXT_TO_IMG,
    returnData=geminiReturnData.IMAGE,
    studioEnumPar="me.mod.smOpUtils.menuPars.fromEnumPar(me.mod.enumPars.StudioImageModels)",
    vertexEnumPar="me.mod.smOpUtils.menuPars.fromEnumPar(me.mod.enumPars.VertexImageModels)",
)
gImgToImg = geminiOP(
    name="Gemini Image to Image",
    opType=geminiOPType.G_IMG_TO_IMG,
    returnData=geminiReturnData.IMAGE,
    studioEnumPar="me.mod.smOpUtils.menuPars.fromEnumPar(me.mod.enumPars.StudioImageModels)",
    vertexEnumPar="me.mod.smOpUtils.menuPars.fromEnumPar(me.mod.enumPars.VertexImageModels)",
)
gTxtToVid = geminiOP(
    name="Gemini Text to Video",
    opType=geminiOPType.G_TXT_TO_VID,
    returnData=geminiReturnData.VIDEO,
    studioEnumPar="me.mod.smOpUtils.menuPars.fromEnumPar(me.mod.enumPars.StudioVeoModels)",
    vertexEnumPar="me.mod.smOpUtils.menuPars.fromEnumPar(me.mod.enumPars.VertexVeoModels)",
)
gImgToVid = geminiOP(
    name="Gemini Image to Video",
    opType=geminiOPType.G_IMG_TO_VID,
    returnData=geminiReturnData.VIDEO,
    studioEnumPar="me.mod.smOpUtils.menuPars.fromEnumPar(me.mod.enumPars.StudioVeoModels)",
    vertexEnumPar="me.mod.smOpUtils.menuPars.fromEnumPar(me.mod.enumPars.VertexVeoModels)",
)
gAudioToTxt = geminiOP(
    name="Gemini Audio to Text",
    opType=geminiOPType.G_AUDIO_TO_TXT,
    returnData=geminiReturnData.TEXT,
    studioEnumPar=geminiObjects.StudioModels.DEPRECATED_GEMINI_3_FLASH_PREVIEW.name,
    vertexEnumPar=geminiObjects.VertexModels.DEPRECATED_GEMINI_3_FLASH_PREVIEW.name,
)
gTxtToAudio = geminiOP(
    name="Gemini Text to Audio",
    opType=geminiOPType.G_TXT_TO_AUDIO,
    returnData=geminiReturnData.AUDIO,
    studioEnumPar="me.mod.smOpUtils.menuPars.fromEnumPar(me.mod.enumPars.StudioAudioModels)",
    vertexEnumPar="me.mod.smOpUtils.menuPars.fromEnumPar(me.mod.enumPars.VertexAudioModels)",
)
gTxtToSpeech = geminiOP(
    name="Gemini Text to Speech",
    opType=geminiOPType.G_TXT_TO_SPEECH,
    returnData=geminiReturnData.AUDIO,
    studioEnumPar=geminiObjects.StudioModels.GEMINI_3_1_FLASH_PREVIEW_TTS.name,
    vertexEnumPar=geminiObjects.VertexModels.GEMINI_3_1_FLASH_PREVIEW_TTS.name,
)
