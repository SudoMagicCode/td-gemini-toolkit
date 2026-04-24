"""
Execute DAT

me - this DAT

Make sure the corresponding toggle is enabled in the Execute DAT.
"""


def onStart():
    """
    Called when the project starts.
    """
    apiKey_server = op("base_comps/base_api_key_server")

    DEFAULT_API_KEY = me.var("DEFAULT_API_KEY")
    UCLA_BASE = me.var("UCLA_BASE_URL")
    UCLA_PREVIEW = me.var("UCLA_PREVIEW_URL")
    UCLA_API_KEY = me.var("UCLA_KEY")

    apiKey_server.mod.apiKeyActions.smOpUtils.createDefaultEndpoint(DEFAULT_API_KEY)
    apiKey_server.mod.apiKeyActions.smOpUtils.addEndpoint(
        "UCLA", "vertex", UCLA_BASE, UCLA_PREVIEW, UCLA_API_KEY
    )

    apiKey_server.par.Distributeendpoints.pulse()
    return


def onCreate():
    """
    Called when the DAT is created.
    """
    return


def onExit():
    """
    Called when the project exits.
    """
    gemini_ops = root.findChildren(tags=["gemini"])
    for each in gemini_ops:
        each.unstore("endpoints")
    return


def onFrameStart(frame: int):
    """
    Called at the start of each frame.

    Args:
            frame: The current frame number
    """
    return


def onFrameEnd(frame: int):
    """
    Called at the end of each frame.

    Args:
            frame: The current frame number
    """
    return


def onPlayStateChange(state: bool):
    """
    Called when the play state changes.

    Args:
            state: False if the timeline was just paused
    """
    return


def onDeviceChange():
    """
    Called when a device change occurs.
    """
    return


def onProjectPreSave():
    """
    Called before the project is saved.
    """
    return


def onProjectPostSave():
    """
    Called after the project is saved.
    """
    return
