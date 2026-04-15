import smOpUtils
import geminiTerminalLogs


def Addapikey(tdPar: Par) -> None:
    '''Parameter function used to add API key from TD Par interface
    '''
    geminiTerminalLogs.msg_formatter("adding api key")
    smOpUtils.get_api_key()


def Clearapikey(tdPar: Par) -> None:
    '''Parameter function used to remove API key from TD Par interface
    '''
    geminiTerminalLogs.msg_formatter("removing api key")
    parent.geminiCOMP.unstore('gemini_apiKey')


def Distributeapikey(tdPar: Par) -> None:
    '''Parameter function used to update API key on all ops with the 
    tag 'gemini' from TD Par interface
    '''
    geminiTerminalLogs.msg_formatter("distributing api key")
    api_key = parent.geminiCOMP.fetch('gemini_apiKey')

    if api_key == None:
        raise ValueError("Missing api key")

    else:
        gemini_ops = smOpUtils.find_gemini_ops_parent_exclusive()

        for each in gemini_ops:
            geminiTerminalLogs.msg_formatter(f"updating {each.name}")
            each.store('gemini_apiKey', api_key)
