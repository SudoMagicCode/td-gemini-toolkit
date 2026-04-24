import copy
import smOpUtils
import geminiTerminalLogs

GEMINI_KEY_NAME = "gemini_apiKey"
modelMap = {
    "base_text_to_text": {
        "studio": "me.mod.smOpUtils.menuPars.fromEnumPar(me.mod.enumPars.StudioTextModels)",
        "vertex": "me.mod.smOpUtils.menuPars.fromEnumPar(me.mod.enumPars.VertexTextModels)",
    },
    "base_text_to_img": {
        "studio": "me.mod.smOpUtils.menuPars.fromEnumPar(me.mod.enumPars.StudioImageModels)",
        "vertex": "me.mod.smOpUtils.menuPars.fromEnumPar(me.mod.enumPars.VertexImageModels)",
    },
    "base_img_to_img": {
        "studio": "me.mod.smOpUtils.menuPars.fromEnumPar(me.mod.enumPars.StudioImageModels)",
        "vertex": "me.mod.smOpUtils.menuPars.fromEnumPar(me.mod.enumPars.VertexImageModels)",
    },
    "base_text_to_video": {
        "studio": "me.mod.smOpUtils.menuPars.fromEnumPar(me.mod.enumPars.StudioVeoModels)",
        "vertex": "me.mod.smOpUtils.menuPars.fromEnumPar(me.mod.enumPars.VertexVeoModels)",
    },
    "base_image_to_video": {
        "studio": "me.mod.smOpUtils.menuPars.fromEnumPar(me.mod.enumPars.StudioVeoModels)",
        "vertex": "me.mod.smOpUtils.menuPars.fromEnumPar(me.mod.enumPars.VertexVeoModels)",
    },
    "base_text_to_audio": {
        "studio": "me.mod.smOpUtils.menuPars.fromEnumPar(me.mod.enumPars.StudioAudioModels)",
        "vertex": "me.mod.smOpUtils.menuPars.fromEnumPar(me.mod.enumPars.VertexAudioModels)",
    },
}


def resolveApiKeyServer() -> None:
    """API Key Resolver - looks for API Key server COMP to pull a key from"""

    # get end point info for the op
    info = resolveEndpointInfo()

    if info == None:
        # if there's no info, check for an API key server
        parent.geminiCOMP.par.Hasapikey = False
        geminiTerminalLogs.msg_formatter(
            f"{parent.geminiCOMP.name} checking for API Key Server"
        )
        _resolveApiKeyServer()

    else:
        if info.get("apiKey") == None or info.get("apiKey") == "":
            parent.geminiCOMP.par.Hasapikey = False
            _resolveApiKeyServer()
        else:
            # has an existing API key, take no action
            geminiTerminalLogs.msg_formatter(
                f"{parent.geminiCOMP.name} has existing API Key, skipping"
            )


def _resolveApiKeyServer():
    # ensure that we have key server to pull a key from
    if hasattr(op, "geminiAPIKeyServer"):
        # get endpoint info
        endpoints = op.geminiAPIKeyServer.fetch("endpoints")
        # add to local storage as deep copy
        parent.geminiCOMP.store("endpoints", copy.deepcopy(endpoints))
        # update pars
        smOpUtils.updateApiEndpointPar()

        # get info and update has apikey state
        info = resolveEndpointInfo()
        if info == None:
            parent.geminiCOMP.par.Hasapikey = False
        else:
            if info.get("apiKey") == None or info.get("apiKey") == "":
                parent.geminiCOMP.par.Hasapikey = False
            else:
                parent.geminiCOMP.par.Hasapikey = True

    else:
        pass


def resolveEndpointInfo(targetOp: OP = parent.geminiCOMP) -> dict:
    """"""
    endpoint_key = targetOp.par.Apiendpoint.eval()

    endPoint_info = targetOp.fetch("endpoints", {})
    storage_info = endPoint_info.get(endpoint_key, {})

    if storage_info == None:
        return None
    else:
        return storage_info


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
            smOpUtils.set_par_state(parent.geminiCOMP, "Hasapikey", False)
        else:
            smOpUtils.set_par_state(parent.geminiCOMP, "Hasapikey", True)
            if parent.geminiCOMP.name in modelMap.keys():
                menuSourceStr = modelMap.get(parent.geminiCOMP.name).get("vertex")
                if info.get("modelType") == "studio":
                    menuSourceStr = modelMap.get(parent.geminiCOMP.name).get("studio")
                smOpUtils.updateMenuSource(parent.geminiCOMP, "Model", menuSourceStr)
            else:
                pass


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
            smOpUtils.updateApiEndpointPar(each)
            info = resolveEndpointInfo(each)
            if info == None:
                each.par.Hasapikey = False
            else:
                if info.get("apiKey") == None or info.get("apiKey") == "":
                    each.par.Hasapikey = False
                else:
                    each.par.Hasapikey = True
