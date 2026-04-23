import smOpUtils
import geminiTerminalLogs

GEMINI_KEY_NAME = "gemini_apiKey"


def resolveApiKeyServer():
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
    info = {"baseURL": "foo", "previewURL": "bar", "apiKey": "bang"}

    return info


def Addapikey(tdPar: Par) -> None:
    """Parameter function used to add API key from TD Par interface"""
    geminiTerminalLogs.msg_formatter("adding api key")
    smOpUtils.get_api_key()


def Clearapikey(tdPar: Par) -> None:
    """Parameter function used to remove API key from TD Par interface"""
    geminiTerminalLogs.msg_formatter("removing api key")
    parent.geminiCOMP.unstore(GEMINI_KEY_NAME)


def Clearallapikeys(tdPar: Par) -> None:
    """Clears all API Keys"""
    gemini_ops = smOpUtils.find_gemini_ops_parent_exclusive()

    for each in gemini_ops:
        geminiTerminalLogs.msg_formatter(f"clearing API Key for {each.name}")
        each.unstore(GEMINI_KEY_NAME)


def Distributeapikey(tdPar: Par) -> None:
    """Parameter function used to update API key on all ops with the
    tag 'gemini' from TD Par interface
    """
    geminiTerminalLogs.msg_formatter("distributing api key")
    api_key = parent.geminiCOMP.fetch(GEMINI_KEY_NAME)

    if api_key == None:
        raise ValueError("Missing api key")

    else:
        gemini_ops = smOpUtils.find_gemini_ops_parent_exclusive()

        for each in gemini_ops:
            geminiTerminalLogs.msg_formatter(f"updating {each.name}")
            each.store(GEMINI_KEY_NAME, api_key)
