from enum import Enum
from geminiObjects import *
from smOpUtils import ModelAsPar

# fmt: off
# NOTE Studio Enum Pars
class StudioTextModels(Enum):
    """
    Gemini Text Models
    """
    GEMINI_3_1_FLASH_LITE_PREVIEW   = ModelAsPar(StudioModels.GEMINI_3_1_FLASH_LITE_PREVIEW, "Gemini 2.5 Pro")
    GEMINI_3_1_PRO_PREVIEW          = ModelAsPar(StudioModels.GEMINI_3_1_PRO_PREVIEW, "Gemini 3 Flash Preview")

class StudioImageModels(Enum):
    """
    Gemini Image Models
    """

    # Actual
    GEMINI_3_PRO_IMAGE_PREVIEW      = ModelAsPar(StudioModels.GEMINI_3_PRO_IMAGE_PREVIEW, "Gemini 3.0 Pro Image Preview")
    GEMINI_3_1_PRO_IMAGE_PREVIEW    = ModelAsPar(StudioModels.GEMINI_3_1_PRO_IMAGE_PREVIEW, "Gemini 3.1 Pro Image Preview")
    GEMINI_3_1_FLASH_IMAGE_PREVIEW  = ModelAsPar(StudioModels.GEMINI_3_1_FLASH_IMAGE_PREVIEW, "Gemini 3.1 Flash Image Preview")

class StudioAudioModels(Enum):
    """
    Gemini Audio Models
    """

    LYRIA_3_CLIP_PREVIEW            = ModelAsPar(StudioModels.LYRIA_3_CLIP_PREVIEW, "Lyria 3 Clip Preview")
    LYRIA_3_PRO_PREVIEW             = ModelAsPar(StudioModels.LYRIA_3_PRO_PREVIEW, "Lyria 3 Pro Preview")


class StudioTTSModels(Enum):
    """
    Gemini TTS Models
    """

    GEMINI_2_5_FLASH_PREVIEW_TTS    = ModelAsPar(StudioModels.GEMINI_2_5_FLASH_PREVIEW_TTS, "Gemini 2.5 Flash Preview TTS")
    GEMINI_2_5_PRO_PREVIEW_TTS      = ModelAsPar(StudioModels.GEMINI_2_5_PRO_PREVIEW_TTS, "Gemini 2.5 Pro Preview TTS")
    GEMINI_3_1_FLASH_PREVIEW_TTS    = ModelAsPar(StudioModels.GEMINI_3_1_FLASH_PREVIEW_TTS, "Gemini 3.1 Flash TTS")



class StudioVeoModels(Enum):
    """
    VEO Video Models
    """

    VEO_3_1_GENERATE_PREVIEW        = ModelAsPar(StudioModels.VEO_3_1_GENERATE_PREVIEW, "VEO 3.1 Generate Preview")
    VEO_3_1_FAST_GENERATE_PREVIEW   = ModelAsPar(StudioModels.VEO_3_1_FAST_GENERATE_PREVIEW, "VEO 3.1 Fast Preview")
    VEO_3_1_LITE_GENERATE_PREVIEW   = ModelAsPar(StudioModels.VEO_3_1_LITE_GENERATE_PREVIEW, "VEO 3.1 Lite Preview")


# NOTE Vertex Enum Pars
class VertexTextModels(Enum):
    """
    Gemini Text Models
    """

    GEMINI_2_5_FLASH                = ModelAsPar(VertexModels.GEMINI_2_5_FLASH, "Gemini 2.5 Flash")
    GEMINI_2_5_PRO                  = ModelAsPar(VertexModels.GEMINI_2_5_PRO, "Gemini 2.5 Pro")
    GEMINI_3_1_FLASH_LITE_PREVIEW   = ModelAsPar(VertexModels.GEMINI_3_1_FLASH_LITE_PREVIEW, "Gemini 3.1 Flash Lite Preview")
    GEMINI_3_1_PRO_PREVIEW          = ModelAsPar(VertexModels.GEMINI_3_1_PRO_PREVIEW, "Gemini 3.1 Pro Preview")    

class VertexImageModels(Enum):
    """
    Gemini Image Models
    """

    # NOTE Depreciated according to google
    # GEMINI_2_5_FLASH_IMAGE          = ModelAsPar(VertexModels.GEMINI_2_5_FLASH_IMAGE, "Gemini 2.5 Flash Image")

    # NOTE removed due to inconsistent return payload
    # IMAGEN_3_0_GENERATE_002         = ModelAsPar(VertexModels.IMAGEN_3_0_GENERATE_002, "Imagen 3.0 Generate 002")
    # IMAGEN_3_0_FAST_GENERATE_001    = ModelAsPar(VertexModels.IMAGEN_3_0_FAST_GENERATE_001, "Imagen 3.0 Fast Generate 001")
    # IMAGEN_4_0_GENERATE_PREDICT     = ModelAsPar(VertexModels.IMAGEN_4_0_GENERATE_PREDICT, "Imagen 4.0 Generate Predict")

    # Actual
    GEMINI_3_PRO_IMAGE_PREVIEW      = ModelAsPar(VertexModels.GEMINI_3_PRO_IMAGE_PREVIEW, "Gemini 3.0 Pro Image Preview")
    GEMINI_3_1_FLASH_IMAGE_PREVIEW  = ModelAsPar(VertexModels.GEMINI_3_1_FLASH_IMAGE_PREVIEW, "Gemini 3.1 Flash Image Preview")

    # NOTE removed due to unavailability from response
    # GEMINI_3_1_PRO_IMAGE_PREVIEW    = ModelAsPar(VertexModels.GEMINI_3_1_PRO_IMAGE_PREVIEW, "Gemini 3.1 Pro Image Preview")


class VertexAudioModels(Enum):
    """
    Gemini Audio Models
    """

    LYRIA_002                       = ModelAsPar(VertexModels.LYRIA_002, "Lyria 002")
    LYRIA_3_CLIP_PREVIEW            = ModelAsPar(VertexModels.LYRIA_3_CLIP_PREVIEW, "Lyria 3 Clip")
    LYRIA_3_PRO_PREVIEW             = ModelAsPar(VertexModels.LYRIA_3_PRO_PREVIEW, "Lyria 3 Pro")


class VertexTTSModels(Enum):
    """
    Gemini TTS Models
    """

    GEMINI_2_5_FLASH_TTS            = ModelAsPar(VertexModels.GEMINI_2_5_FLASH_TTS, "Gemini 2.5 Flash TTS")
    GEMINI_2_5_FLASH_PREVIEW_TTS    = ModelAsPar(VertexModels.GEMINI_2_5_FLASH_PREVIEW_TTS, "Gemini 2.5 Pro Preview TTS")
    GEMINI_2_5_PRO_TTS              = ModelAsPar(VertexModels.GEMINI_2_5_PRO_TTS, "Gemini 2.5 Pro TTS")
    GEMINI_3_1_FLASH_PREVIEW_TTS    = ModelAsPar(VertexModels.GEMINI_3_1_FLASH_PREVIEW_TTS, "Gemini 3.1 Flash Preview TTS")


class VertexVeoModels(Enum):
    """
    VEO Video Models
    """

    VEO_2_0_GENERATE_001            = ModelAsPar(VertexModels.VEO_2_0_GENERATE_001, "VEO 2.0 Generate 001")
    VEO_3_0_GENERATE_001            = ModelAsPar(VertexModels.VEO_3_0_GENERATE_001, "VEO 3.0 Generate 001")
    VEO_3_0_FAST_GENERATE_001       = ModelAsPar(VertexModels.VEO_3_0_FAST_GENERATE_001, "VEO 3.0 Fast Generate 001")
    VEO_3_1_GENERATE_001            = ModelAsPar(VertexModels.VEO_3_1_GENERATE_001, "VEO 3.1 Generate 001")
    VEO_3_1_FAST_GENERATE_001       = ModelAsPar(VertexModels.VEO_3_1_FAST_GENERATE_001, "VEO 3.1 Fast Generate 001")
    VEO_3_1_LITE_GENERATE_001       = ModelAsPar(VertexModels.VEO_3_1_LITE_GENERATE_001, "VEO 3.1 Lite Generate 001")

# fmt: on
