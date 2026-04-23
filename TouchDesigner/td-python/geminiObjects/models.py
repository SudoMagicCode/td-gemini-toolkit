from dataclasses import dataclass
from enum import StrEnum, Enum


class Model(object):
    def __init__(self, modelLookup: str, isPreview: bool):
        self._model = modelLookup
        self._preview = isPreview

    @property
    def model(self) -> str:
        return self._model

    @property
    def isPreview(self) -> bool:
        return self._preview


class Models(StrEnum):
    """Gemini Models"""

    # Preview models
    GEMINI_3_1_FLASH_PREVIEW_TTS = Model(
        "models/gemini-3.1-flash-tts-preview",
        True,
    )
    GEMINI_3_1_PRO_PREVIEW = Model(
        "models/gemini-3.1-pro-preview",
        True,
    )
    GEMINI_3_1_PRO_IMAGE_PREVIEW = Model(
        "models/gemini-3.1-pro-image-preview",
        True,
    )
    GEMINI_3_0_PRO_IMAGE_PREVIEW = Model(
        "models/gemini-3-pro-image-preview",
        True,
    )
    GEMINI_3_FLASH_PREVIEW = Model(
        "models/gemini-3-flash-preview",
        True,
    )
    GEMINI_3_1_FLASH_LITE_PREVIEW = Model(
        "models/gemini-3.1-flash-lite-preview",
        True,
    )
    GEMINI_3_1_FLASH_IMAGE_PREVIEW = Model(
        "models/gemini-3.1-flash-image-preview",
        True,
    )
    GEMINI_3_1_PREVIEW_TTS = Model(
        "models/gemini-3.1-flash-tts-preview",
        True,
    )
    GEMINI_2_5_FLASH_PREVIEW_TTS = Model(
        "gemini-2.5-flash-preview-tts",
        False,
    )
    GEMINI_2_5_PRO_PREVIEW_TTS = Model(
        "gemini-2.5-pro-preview-tts",
        False,
    )
    VEO_3_1_GENERATE_PREVIEW = Model(
        "models/veo-3.1-generate-preview",
        True,
    )
    VEO_3_1_FAST_GENERATE_PREVIEW = Model(
        "models/veo-3.1-fast-generate-preview",
        True,
    )
    VEO_3_1_LITE_GENERATE_PREVIEW = Model(
        "models/veo-3.1-lite-generate-preview",
        True,
    )
    VEO_3_0_GENERATE_PREVIEW = Model(
        "models/veo-3.0-generate-001",
        False,
    )
    LYRIA_3_CLIP_PREVIEW = Model(
        "models/lyria-3-clip-preview",
        True,
    )
    LYRIA_3_PRO_PREVIEW = Model(
        "models/lyria-3-pro-preview",
        True,
    )

    # enterprise models
    GEMINI_2_5_FLASH = Model(
        "models/gemini-2.5-flash",
        False,
    )
    GEMINI_2_5_FLASH_IMAGE = Model(
        "models/gemini-2.5-flash-image",
        False,
    )
    GEMINI_2_5_FLASH_TTS = Model(
        "models/gemini-2.5-flash-tts",
        False,
    )
    GEMINI_2_5_PRO = Model(
        "models/gemini-2.5-pro",
        False,
    )
    GEMINI_2_5_PRO_TTS = Model(
        "models/gemini-2.5-flash-tts",
        False,
    )
    IMAGEN_3_0_GENERATE_002 = Model(
        "models/imagen-3.0-generate-002",
        False,
    )
    IMAGEN_3_0_FAST_GENERATE_001 = Model(
        "models/imagen-3.0-fast-generate-001",
        False,
    )
    IMAGEN_4_0_GENERATE_PREDICT = Model(
        "models/imagen-4.0-generate-001",
        False,
    )
    LYRIA_002 = Model(
        "models/lyria-002",
        False,
    )
    VEO_2_0_GENERATE_001 = Model(
        "models/veo-2.0-generate-001",
        False,
    )
    VEO_3_0_GENERATE_001 = Model(
        "models/veo-3.0-generate-001",
        False,
    )
    VEO_3_0_FAST_GENERATE_001 = Model(
        "models/veo-3.0-fast-generate-001",
        False,
    )
    VEO_3_1_GENERATE_001 = Model(
        "models/veo-3.1-generate-001",
        False,
    )
    VEO_3_1_FAST_GENERATE_001 = Model(
        "models/veo-3.1-fast-generate-001",
        False,
    )
    VEO_3_1_LITE_GENERATE_001 = Model(
        "models/veo-3.1-lite-generate-001",
        False,
    )
