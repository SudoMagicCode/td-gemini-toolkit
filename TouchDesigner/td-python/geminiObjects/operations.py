from enum import StrEnum


class RpcOperations(StrEnum):
    """RPC Call Operations"""

    GENERATE_CONTENT = "generateContent"
    PREDICT_LONG_RUNNING = "predictLongRunning"
    PREDICT = "predict"
    STREAM_GENERATE_CONTENT = "streamGenerateContent"
    FETCH_PREDICT_OPERATION = "fetchPredictOperation"
