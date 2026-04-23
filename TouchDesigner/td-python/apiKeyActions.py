import copy
import smOpUtils
import geminiTerminalLogs

GEMINI_KEY_NAME = "gemini_apiKey"


def resolveApiKeyServer() -> None:
    """API Key Resolver - looks for API Key server COMP to pull a key from"""
    # if component has existing API key, skip
    if parent.geminiCOMP.par.Hasapikey.eval():
        geminiTerminalLogs.msg_formatter(
            f"{parent.geminiCOMP.name} has existing API Key, skipping"
        )

    # if component has no api key, check for API Key Server
    else:
        geminiTerminalLogs.msg_formatter(
            f"{parent.geminiCOMP.name} checking for API Key Server"
        )
        # ensure that we have key server to pull a key from
        if hasattr(op, "geminiAPIKeyServer"):
            # check to see if the key server has a valid key
            if op.geminiAPIKeyServer.fetch(GEMINI_KEY_NAME, None) not in [None, ""]:
                # store valid key
                gemini_key = op.geminiAPIKeyServer.fetch(GEMINI_KEY_NAME)
                parent.geminiCOMP.store(GEMINI_KEY_NAME, gemini_key)
                geminiTerminalLogs.msg_formatter(
                    f"{parent.geminiCOMP.name} applying API Key", indent=1
                )
        else:
            pass


def resolveEndpointInfo() -> dict:
    """"""
    endpoint_key = parent.geminiCOMP.par.Apiendpoint.eval()
    print(endpoint_key)

    endPoint_info = parent.geminiCOMP.fetch("endpoints", {})
    storage_info = endPoint_info.get(endpoint_key, {})

    if storage_info == None:
        return None
    else:
        return storage_info


def addEndpoint(name: str, baseUrl: str, previewUrl: str, apiKey: str) -> None:
    newEndpoint = smOpUtils.apiEndpoint(name, baseUrl, previewUrl, apiKey)
    endpoints = parent.geminiCOMP.fetch("endpoints", {})


def Adddefaultapikey(tdPar: Par) -> None:
    """Parameter function used to add API key from TD Par interface"""
    geminiTerminalLogs.msg_formatter("adding api key")
    smOpUtils.get_api_key()


def Clearapikey(tdPar: Par) -> None:
    """Parameter function used to remove API key from TD Par interface"""
    geminiTerminalLogs.msg_formatter("removing api key")
    parent.geminiCOMP.unstore(GEMINI_KEY_NAME)


def Clearendpoints(tdPar: Par) -> None:
    """Parameter function used to remove API key from TD Par interface"""
    geminiTerminalLogs.msg_formatter("removing all api endpoints")
    parent.geminiCOMP.unstore("endpoints")
    smOpUtils.updateApiEndpointPar()


def Clearallendpoints(tdPar: Par) -> None:
    """Clears all API Keys"""
    gemini_ops = smOpUtils.find_gemini_ops_parent_exclusive()

    for each in gemini_ops:
        geminiTerminalLogs.msg_formatter(f"clearing API Key for {each.name}")
        each.unstore("endpoints")
        smOpUtils.updateApiEndpointPar(each)


def Apiendpoint(tdPar: Par) -> None:
    info = resolveEndpointInfo()

    if info == None:
        parent.geminiCOMP.par.Hasapikey = False
    else:
        if info.get("apiKey") == None or info.get("apiKey") == "":
            parent.geminiCOMP.par.Hasapikey = False
        else:
            parent.geminiCOMP.par.Hasapikey = True


def Distributeendpoints(tdPar: Par) -> None:
    """Parameter function used to update API key on all ops with the
    tag 'gemini' from TD Par interface
    """
    geminiTerminalLogs.msg_formatter("distributing Endpoints")
    localEndpoints = parent.geminiCOMP.fetch("endpoints", None)
    endPointCopy = copy.deepcopy(localEndpoints)

    if localEndpoints == None:
        raise ValueError("No endpoints to distribute")

    else:
        gemini_ops = smOpUtils.find_gemini_ops_parent_exclusive()

        for each in gemini_ops:
            geminiTerminalLogs.msg_formatter(f"updating {each.name}")
            each.store("endpoints", endPointCopy)
