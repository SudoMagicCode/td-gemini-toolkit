from enum import Enum
from geminiObjects import Models
from smOpUtils import ModelAsPar


class TextModels(Enum):
    """
    Gemini Text Models
    """

    GEMINI_3_1 = ModelAsPar(Models.GEMINI_3_1_PRO_PREVIEW, "Gemini 3.1")
    GEMINI_3_1_FLASH = ModelAsPar(Models.GEMINI_3_FLASH_PREVIEW, "Gemini 3 Flash")
    GEMINI_3_1_FLASH_LITE = ModelAsPar(
        Models.GEMINI_3_1_FLASH_LITE_PREVIEW, "Gemini 3.1 Flash Lite"
    )


class ImageModels(Enum):
    """
    Gemini Text Models
    """

    GEMINI_3_0_PRO_IMAGE_PREVIEW = ModelAsPar(
        Models.GEMINI_3_0_PRO_IMAGE_PREVIEW, "Nano Banana Pro"
    )
    GEMINI_3_1_FLASH_IMAGE_PREVIEW = ModelAsPar(
        Models.GEMINI_3_1_FLASH_IMAGE_PREVIEW, "Nano Banana 2"
    )


class AudioModels(Enum):
    """
    Gemini Audio Models
    """

    LYRIA_3_CLIP_PREVIEW = ModelAsPar(Models.LYRIA_3_CLIP_PREVIEW, "Lyria 3 Clip")
    LYRIA_3_PRO_PREVIEW = ModelAsPar(Models.LYRIA_3_PRO_PREVIEW, "Lyria 3 Pro")


class VeoModels(Enum):
    """
    VEO Models
    """

    VEO_3_1_GENERATE_PREVIEW = ModelAsPar(Models.VEO_3_1_GENERATE_PREVIEW, "VEO 3.1")
    VEO_3_1_FAST_GENERATE_PREVIEW = ModelAsPar(
        Models.VEO_3_1_FAST_GENERATE_PREVIEW, "VEO 3.1 Fast"
    )
    VEO_3_1_LITE_GENERATE_PREVIEW = ModelAsPar(
        Models.VEO_3_1_LITE_GENERATE_PREVIEW, "VEO 3.1 Lite"
    )
    VEO_3_0_GENERATE_PREVIEW = ModelAsPar(Models.VEO_3_0_GENERATE_PREVIEW, "VEO 3.0")
