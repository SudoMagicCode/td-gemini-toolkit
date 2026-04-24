import models
import operations


def CreatePath(model: models.VertexModels, operation: operations.RpcOperations) -> str:
    return f"{model}:{operation}"


def CreateRawPath(name: str) -> str:
    return f"{name}"


def CreatePathWithOperation(name: str, operation: operations.RpcOperations) -> str:
    return f"{name}:{operation}"
