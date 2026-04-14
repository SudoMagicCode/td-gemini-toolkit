from enum import StrEnum

class Models(StrEnum):
    '''Gemini Models
    '''
    GEMINI_2_5_FLASH_PREVIEW_TTS = "models/gemini-2.5-flash-preview-tts"
    GEMINI_3_1_PRO_PREVIEW = "models/gemini-3.1-pro-preview"
    GEMINI_3_1_PRO_IMAGE_PREVIEW = "models/gemini-3.1-pro-image-preview"
    GEMINI_3_FLASH_PREVIEW = "models/gemini-3-flash-preview"
    GEMINI_3_1_FLASH_IMAGE_PREVIEW = "models/gemini-3.1-flash-image-preview"
    VEO_3_1_GENERATE_PREVIEW= "models/veo-3.1-generate-preview"
    LYRIA_3_CLIP_PREVIEW = "models/lyria-3-clip-preview"
    IMAGEN_4_0_GENERATE_PREDICT = "models/imagen-4.0-generate-001"
    