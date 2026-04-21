"""
Execute DAT

me - this DAT

Make sure the corresponding toggle is enabled in the Execute DAT.
"""


def onStart():
    """
    Called when the project starts.
    """
    gemini_ops = root.findChildren(tags=["gemini"])
    api_key = me.var("GEMINI_API_KEY")
    for each in gemini_ops:
        each.store("gemini_apiKey", api_key)
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
        each.unstore("gemini_apiKey")
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
