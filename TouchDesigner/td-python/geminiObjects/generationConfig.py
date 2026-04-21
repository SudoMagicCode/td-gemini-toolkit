from enum import StrEnum


class GenerationAspectRatio(StrEnum):
    """Gemini Aspect Ratios"""

    ASPECT_1_1 = "1:1"
    ASPECT_1_4 = "1:4"
    ASPECT_1_8 = "1:8"
    ASPECT_2_3 = "2:3"
    ASPECT_3_2 = "3:2"
    ASPECT_3_4 = "3:4"
    ASPECT_4_1 = "4:1"
    ASPECT_4_3 = "4:3"
    ASPECT_4_5 = "4:5"
    ASPECT_5_4 = "5:4"
    ASPECT_8_1 = "8:1"
    ASPECT_9_16 = "9:16"
    ASPECT_16_9 = "16:9"
    ASPECT_21_9 = "21:9"


class GenerationImageSize(StrEnum):
    """Gemini Image Size"""

    RESOLUTION_512 = "512"
    RESOLUTION_1K = "1K"
    RESOLUTION_2K = "2K"
    RESOLUTION_4K = "4K"


class GenerationThinkingLevel(StrEnum):
    """Gemini Thinking levels"""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
