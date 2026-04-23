import models
import operations


GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta"


def CreateEndpoint(
    model: models.Models, operation: operations.RpcOperations, base_url: str = None
) -> str:
    if base_url is not None:
        return f"{base_url}/{model}:{operation}"
    return f"{GEMINI_BASE_URL}/{model}:{operation}"


def CreateRawEndpoint(name: str, base_url: str = None) -> str:
    if base_url is not None:
        return f"{base_url}/{name}"
    return f"{GEMINI_BASE_URL}/{name}"
