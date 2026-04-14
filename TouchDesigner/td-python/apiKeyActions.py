import smOpUtils


def Addapikey(tdPar: Par) -> None:
    print("adding api key")
    smOpUtils.get_api_key()


def Clearapikey(tdPar: Par) -> None:
    print("removing api key")
    parent.geminiCOMP.unstore('gemini_apiKey')


def Distributeapikey(tdPar: Par) -> None:
    print("distributing api key")
    api_key = parent.geminiCOMP.fetch('gemini_apiKey')

    if api_key == None:
        raise ValueError("Missing api key")

    else:
        gemini_ops = smOpUtils.find_gemini_ops_parent_exclusive()

        for each in gemini_ops:
            print(f"updating {each.name}")
            each.store('gemini_apiKey', api_key)
