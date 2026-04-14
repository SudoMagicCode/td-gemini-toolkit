api_pop_dialog = parent.geminiCOMP.op('base_assets/popDialog')


def find_gemini_ops() -> list[OP]:
    '''Returns a list of all ops with the `gemini` tag
    '''
    gemini_ops = root.findChildren(tags=['gemini'])
    return gemini_ops


def find_gemini_ops_parent_exclusive() -> list[OP]:
    '''Returns a list of all ops with the `gemini` tag, excluding the parent of the calling op
    '''
    gemini_ops = find_gemini_ops()
    return [each for each in gemini_ops if each.name != parent.geminiCOMP.name]


def get_api_key() -> None:

    def pop_dialog_cb(info: dict) -> None:
        buttonIndex = info.get('buttonNum')
        api_key = info.get('enteredText')
        if buttonIndex == 1:
            parent.geminiCOMP.store('gemini_apiKey', api_key)

        else:
            return None

    api_pop_dialog.Open(callback=pop_dialog_cb)
