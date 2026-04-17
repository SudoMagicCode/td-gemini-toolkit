from enum import Enum
from geminiObjects import Models
from smOpUtils import ModelAsPar


class TextModels(Enum):
    GEMINI_3_1 = ModelAsPar(
        Models.GEMINI_3_1_PRO_PREVIEW, "Gemini 3.1")
    GEMINI_3_1_FLASH = ModelAsPar(
        Models.GEMINI_3_FLASH_PREVIEW, "Gemini 3.1 Flash")
    GEMINI_3_1_FLASH_LITE = ModelAsPar(
        Models.GEMINI_3_FLASH_LITE_PREVIEW, "Gemini 3.1 Flash Lite")
