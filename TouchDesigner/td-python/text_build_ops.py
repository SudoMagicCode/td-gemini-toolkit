

def clear_api_keys():
    gemini_ops = root.findChildren(tags=['gemini'])
    for each in gemini_ops:
        each.unstore('gemini_apiKey')


def build_ops():
    clear_api_keys()


build_ops()
