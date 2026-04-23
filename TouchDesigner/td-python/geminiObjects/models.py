from dataclasses import dataclass
from enum import StrEnum, Enum


class Models(StrEnum):
    """Gemini Models"""

    # Preview models
    GEMINI_3_1_FLASH_PREVIEW_TTS = "models/gemini-3.1-flash-tts-preview"
    GEMINI_3_1_PRO_PREVIEW = "models/gemini-3.1-pro-preview"
    GEMINI_3_1_PRO_IMAGE_PREVIEW = "models/gemini-3.1-pro-image-preview"
    GEMINI_3_0_PRO_IMAGE_PREVIEW = "models/gemini-3-pro-image-preview"
    GEMINI_3_FLASH_PREVIEW = "models/gemini-3-flash-preview"
    GEMINI_3_1_FLASH_LITE_PREVIEW = "models/gemini-3.1-flash-lite-preview"
    GEMINI_3_1_FLASH_IMAGE_PREVIEW = "models/gemini-3.1-flash-image-preview"
    GEMINI_3_1_PREVIEW_TTS = "models/gemini-3.1-flash-tts-preview"
    GEMINI_2_5_FLASH_PREVIEW_TTS = "gemini-2.5-flash-preview-tts"
    GEMINI_2_5_PRO_PREVIEW_TTS = "gemini-2.5-pro-preview-tts"
    VEO_3_1_GENERATE_PREVIEW = "models/veo-3.1-generate-preview"
    VEO_3_1_FAST_GENERATE_PREVIEW = "models/veo-3.1-fast-generate-preview"
    VEO_3_1_LITE_GENERATE_PREVIEW = "models/veo-3.1-lite-generate-preview"
    VEO_3_0_GENERATE_PREVIEW = "models/veo-3.0-generate-001"
    LYRIA_3_CLIP_PREVIEW = "models/lyria-3-clip-preview"
    LYRIA_3_PRO_PREVIEW = "models/lyria-3-pro-preview"

    # enterprise models
    GEMINI_2_5_FLASH = "models/gemini-2.5-flash"
    GEMINI_2_5_FLASH_IMAGE = "models/gemini-2.5-flash-image"
    GEMINI_2_5_FLASH_TTS = "models/gemini-2.5-flash-tts"
    GEMINI_2_5_PRO = "models/gemini-2.5-pro"
    GEMINI_2_5_PRO_TTS = "models/gemini-2.5-flash-tts"
    IMAGEN_3_0_GENERATE_002 = "models/imagen-3.0-generate-002"
    IMAGEN_3_0_FAST_GENERATE_001 = "models/imagen-3.0-fast-generate-001"
    IMAGEN_4_0_GENERATE_PREDICT = "models/imagen-4.0-generate-001"
    LYRIA_002 = "models/lyria-002"
    VEO_2_0_GENERATE_001 = "models/veo-2.0-generate-001"
    VEO_3_0_GENERATE_001 = "models/veo-3.0-generate-001"
    VEO_3_0_FAST_GENERATE_001 = "models/veo-3.0-fast-generate-001"
    VEO_3_1_GENERATE_001 = "models/veo-3.1-generate-001"
    VEO_3_1_FAST_GENERATE_001 = "models/veo-3.1-fast-generate-001"
    VEO_3_1_LITE_GENERATE_001 = "models/veo-3.1-lite-generate-001"
