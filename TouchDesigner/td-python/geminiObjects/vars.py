import models
import operations

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta"

def CreateEndpoint(model: models.Models, operation: operations.RpcOperations) -> str:
	return f'{GEMINI_BASE_URL}/{model}:{operation}' 