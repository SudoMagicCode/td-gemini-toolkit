from dataclasses import dataclass
from enum import StrEnum, Enum


class GeminiModel(object):
    def __init__(self, modelLookup: str, isPreview: bool):
        self._model = modelLookup
        self._preview = isPreview

    @property
    def model(self) -> str:
        return self._model

    @property
    def isPreview(self) -> bool:
        return self._preview


# fmt: off
class StudioModels(Enum):

    """Gemini Models"""
    # Preview models
    
    # text models
    GEMINI_3_1_FLASH_LITE_PREVIEW       = GeminiModel("models/gemini-3.1-flash-lite-preview", True)
    GEMINI_3_1_PRO_PREVIEW              = GeminiModel("models/gemini-3.1-pro-preview", True)

    # image models
    GEMINI_3_PRO_IMAGE_PREVIEW          = GeminiModel("models/gemini-3-pro-image-preview", True)
    GEMINI_3_1_FLASH_IMAGE_PREVIEW      = GeminiModel("models/gemini-3.1-flash-image-preview", True)

    # audio models
    LYRIA_3_CLIP_PREVIEW                = GeminiModel("models/lyria-3-clip-preview", True)
    LYRIA_3_PRO_PREVIEW                 = GeminiModel("models/lyria-3-pro-preview", True)

    # tts models
    GEMINI_2_5_FLASH_PREVIEW_TTS        = GeminiModel("models/gemini-2.5-flash-preview-tts", True)
    GEMINI_2_5_PRO_PREVIEW_TTS          = GeminiModel("models/gemini-2.5-pro-preview-tts", True)
    GEMINI_3_1_FLASH_PREVIEW_TTS        = GeminiModel("models/gemini-3.1-flash-tts-preview", True)

    # video models
    VEO_3_1_GENERATE_PREVIEW            = GeminiModel("models/veo-3.1-generate-preview", True)
    VEO_3_1_FAST_GENERATE_PREVIEW       = GeminiModel("models/veo-3.1-fast-generate-preview", True)
    VEO_3_1_LITE_GENERATE_PREVIEW       = GeminiModel("models/veo-3.1-lite-generate-preview", True)



class VertexModels(Enum):

    """Gemini Models"""
    # enterprise models
    
    # text models
    GEMINI_2_5_FLASH                    = GeminiModel("models/gemini-2.5-flash", False)
    GEMINI_2_5_FLASH_IMAGE              = GeminiModel("models/gemini-2.5-flash-image", False)
    GEMINI_2_5_PRO                      = GeminiModel("models/gemini-2.5-pro", False)
    GEMINI_3_1_FLASH_LITE_PREVIEW       = GeminiModel("models/gemini-3.1-flash-lite-preview", True)
    GEMINI_3_1_PRO_PREVIEW              = GeminiModel("models/gemini-3.1-pro-preview", True)
    
    # image models
    GEMINI_3_1_FLASH_IMAGE_PREVIEW      = GeminiModel("models/gemini-3.1-flash-image-preview", True)
    GEMINI_3_PRO_IMAGE_PREVIEW          = GeminiModel("models/gemini-3-pro-image-preview", True)
    IMAGEN_3_0_GENERATE_002             = GeminiModel("models/imagen-3.0-generate-002", False)
    IMAGEN_3_0_FAST_GENERATE_001        = GeminiModel("models/imagen-3.0-fast-generate-001", False)
    IMAGEN_4_0_GENERATE_PREDICT         = GeminiModel("models/imagen-4.0-generate-001", False)

    # audio models 
    LYRIA_002                           = GeminiModel("models/lyria-002", False)
    LYRIA_3_CLIP_PREVIEW                = GeminiModel("models/lyria-3-clip-preview", True)
    LYRIA_3_PRO_PREVIEW                 = GeminiModel("models/lyria-3-pro-preview", True)

    # tts models
    GEMINI_2_5_FLASH_TTS                = GeminiModel("models/gemini-2.5-flash-tts", False)
    GEMINI_2_5_FLASH_PREVIEW_TTS        = GeminiModel("models/gemini-2.5-flash-preview-tts", True)
    GEMINI_2_5_PRO_TTS                  = GeminiModel("models/gemini-2.5-flash-tts", False)
    GEMINI_3_1_FLASH_PREVIEW_TTS        = GeminiModel("models/gemini-3.1-flash-tts-preview", True)
    
    # video models
    VEO_2_0_GENERATE_001                = GeminiModel("models/veo-2.0-generate-001", False)
    VEO_3_0_GENERATE_001                = GeminiModel("models/veo-3.0-generate-001", False)
    VEO_3_0_FAST_GENERATE_001           = GeminiModel("models/veo-3.0-fast-generate-001", False)
    VEO_3_1_GENERATE_001                = GeminiModel("models/veo-3.1-generate-001", False)
    VEO_3_1_FAST_GENERATE_001           = GeminiModel("models/veo-3.1-fast-generate-001", False)
    VEO_3_1_LITE_GENERATE_001           = GeminiModel("models/veo-3.1-lite-generate-001", False)
# fmt: on
