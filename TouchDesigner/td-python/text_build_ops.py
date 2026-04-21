def clear_api_keys():
    gemini_ops = root.findChildren(tags=["gemini"])
    for each in gemini_ops:
        each.unstore("gemini_apiKey")


def build_ops():
    clear_api_keys()
    op("base_save_for_release").par.Package.pulse()


build_ops()
