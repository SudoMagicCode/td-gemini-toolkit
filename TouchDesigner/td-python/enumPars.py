from enum import Enum
from geminiObjects import VertexModels
from smOpUtils import ModelAsPar

# fmt: off
class TextModels(Enum):
    """
    Gemini Text Models
    """

    GEMINI_2_5_FLASH        = ModelAsPar(VertexModels.GEMINI_2_5_FLASH, "Gemini 2.5 Flash")
    GEMINI_2_5_PRO          = ModelAsPar(VertexModels.GEMINI_2_5_PRO, "Gemini 2.5 Pro")
    GEMINI_3_FLASH_PREVIEW  = ModelAsPar(VertexModels.GEMINI_3_FLASH_PREVIEW, "Gemini 3 Flash Preview")
    GEMINI_3_1_PRO_PREVIEW  = ModelAsPar(VertexModels.GEMINI_3_1_PRO_PREVIEW, "Gemini 3.1 Pro Preview")
    GEMINI_3_1_FLASH_LITE   = ModelAsPar(VertexModels.GEMINI_3_1_FLASH_LITE_PREVIEW, "Gemini 3.1 Flash Lite Preview")


class ImageModels(Enum):
    """
    Gemini Image Models
    """

    # Vanity - these models are duplicates of other models with vanity marketing names
    NANO_BANANA_PRO     = ModelAsPar(VertexModels.GEMINI_3_PRO_IMAGE_PREVIEW, "Nano Banana Pro")
    NANO_BANANA_2       = ModelAsPar(VertexModels.GEMINI_3_1_FLASH_IMAGE_PREVIEW, "Nano Banana 2")

    # Actual
    GEMINI_3_0_PRO_IMAGE_PREVIEW    = ModelAsPar(VertexModels.GEMINI_3_PRO_IMAGE_PREVIEW, "Gemini 3.0 Pro Image Preview")
    GEMINI_3_1_PRO_IMAGE_PREVIEW    = ModelAsPar(VertexModels.GEMINI_3_PRO_IMAGE_PREVIEW, "Gemini 3.1 Pro Image Preview")
    GEMINI_3_1_FLASH_IMAGE_PREVIEW  = ModelAsPar(VertexModels.GEMINI_3_1_FLASH_IMAGE_PREVIEW, "Gemini 3.1 Flash Image Preview")
    GEMINI_2_5_FLASH_IMAGE          = ModelAsPar(VertexModels.GEMINI_2_5_FLASH_IMAGE, "Gemini 2.5 Flash Image")
    IMAGEN_3_0_GENERATE_002         = ModelAsPar(VertexModels.IMAGEN_3_0_GENERATE_002, "Imagen 3.0 Generate 002")
    IMAGEN_3_0_FAST_GENERATE_001    = ModelAsPar(VertexModels.IMAGEN_3_0_FAST_GENERATE_001, "Imagen 3.0 Fast Generate 001")
    IMAGEN_4_0_GENERATE_PREDICT     = ModelAsPar(VertexModels.IMAGEN_4_0_GENERATE_PREDICT, "Imagen 4.0 Generate Predict")


class AudioModels(Enum):
    """
    Gemini Audio Models
    """

    LYRIA_3_CLIP_PREVIEW    = ModelAsPar(VertexModels.LYRIA_3_CLIP_PREVIEW, "Lyria 3 Clip")
    LYRIA_3_PRO_PREVIEW     = ModelAsPar(VertexModels.LYRIA_3_PRO_PREVIEW, "Lyria 3 Pro")
    LYRIA_002               = ModelAsPar(VertexModels.LYRIA_002, "Lyria 002")


class TTSModels(Enum):
    """
    Gemini TTS Models
    """

    GEMINI_2_5_FLASH_PREVIEW_TTS    = ModelAsPar(VertexModels.GEMINI_2_5_FLASH_TTS, "Gemini 2.5 Flash Preview TTS")
    GEMINI_2_5_PRO_PREVIEW_TTS      = ModelAsPar(VertexModels.GEMINI_2_5_PRO_PREVIEW_TTS, "Gemini 2.5 Pro Preview TTS")
    GEMINI_2_5_FLASH_TTS            = ModelAsPar(VertexModels.GEMINI_2_5_FLASH_TTS, "Gemini 2.5 Flash TTS")
    GEMINI_2_5_PRO_TTS              = ModelAsPar(VertexModels.GEMINI_2_5_PRO_TTS, "Gemini 2.5 Pro TTS")
    GEMINI_3_1_FLASH_PREVIEW_TTS          = ModelAsPar(VertexModels.GEMINI_3_1_FLASH_PREVIEW_TTS, "Gemini 3.1 Flash Preview TTS")


class VeoModels(Enum):
    """
    VEO Video Models
    """

    VEO_3_1_GENERATE_PREVIEW        = ModelAsPar(VertexModels.VEO_3_1_GENERATE_PREVIEW, "VEO 3.1 Preview")
    VEO_3_1_FAST_GENERATE_PREVIEW   = ModelAsPar(VertexModels.VEO_3_1_FAST_GENERATE_PREVIEW, "VEO 3.1 Fast Preview")
    VEO_3_1_LITE_GENERATE_PREVIEW   = ModelAsPar(VertexModels.VEO_3_1_LITE_GENERATE_PREVIEW, "VEO 3.1 Lite Preview")

    VEO_2_0_GENERATE_001            = ModelAsPar(VertexModels.VEO_2_0_GENERATE_001, "VEO 2.0 Generate 001")
    VEO_3_0_GENERATE_001            = ModelAsPar(VertexModels.VEO_3_0_GENERATE_001, "VEO 3.0 Generate 001")
    VEO_3_0_FAST_GENERATE_001       = ModelAsPar(VertexModels.VEO_3_0_FAST_GENERATE_001, "VEO 3.0 Fast Generate 001")

    # NOTE not available for consumer API keys
    # VEO_3_1_GENERATE_001            = ModelAsPar(Models.VEO_3_1_GENERATE_001, "VEO 3.1 Generate 001")
    # VEO_3_1_FAST_GENERATE_001       = ModelAsPar(Models.VEO_3_1_FAST_GENERATE_001, "VEO 3.1 Fast Generate 001")
    # VEO_3_1_LITE_GENERATE_001       = ModelAsPar(Models.VEO_3_1_LITE_GENERATE_001, "VEO 3.1 Lite Generate 001")

# fmt: on
