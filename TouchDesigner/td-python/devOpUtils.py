from opDefaults import defaults


def QuitProject():
    print("QUITTING")


def clear_endpoints(targetOp: OP):
    try:
        targetOp.par.Apiendpoint.menuNames = []
        targetOp.par.Apiendpoint.menuLabels = []
    except Exception as e:
        pass


def set_defaults():
    # loop through each operator
    for each_op, pars_dict in defaults.items():
        target_op = op(each_op)
        print(target_op)
        # loop though defaults
        for each_par, value in pars_dict.items():
            # set default
            print(each_par, value)
            print(target_op.par[each_par])
            target_op.par[each_par].default = value
            # set par to default value
            target_op.par[each_par] = value

        clear_endpoints(target_op)


def clear_output_buffers():
    op("base_comps/base_text_to_text/text_output_buffer").clear()
    op("base_comps/base_text_to_chat").par.Clearchathistory.pulse()
    op("base_comps/base_img_to_text/text_output_buffer").clear()
    op("base_comps/base_audio_to_text/text_output_buffer").clear()


def clear_storage():
    op("base_comps/base_text_to_text/text_output_buffer").unstore("metadata")

    op("base_comps/base_text_to_chat/fifo1").unstore("metadata")

    op("base_comps/base_img_to_text/text_output_buffer").unstore("metadata")

    op("base_comps/base_img_to_img/script1").unstore("image_data")
    op("base_comps/base_img_to_img/script1").unstore("metadata")

    op("base_comps/base_text_to_img/script1").unstore("image_data")
    op("base_comps/base_text_to_img/script1").unstore("metadata")

    op("base_comps/base_audio_to_text/text_output_buffer").unstore("metadata")


def set_endpoints():

    apiKey_server = op.geminiAPIKeyServer

    DEFAULT_API_KEY = me.var("DEFAULT_API_KEY")
    UCLA_BASE = me.var("UCLA_BASE_URL")
    UCLA_PREVIEW = me.var("UCLA_PREVIEW_URL")
    UCLA_API_KEY = me.var("UCLA_KEY")

    apiKey_server.mod.apiKeyActions.smOpUtils.createDefaultEndpoint(DEFAULT_API_KEY)
    apiKey_server.mod.apiKeyActions.smOpUtils.addEndpoint(
        "UCLA", "vertex", UCLA_BASE, UCLA_PREVIEW, UCLA_API_KEY
    )

    apiKey_server.par.Distributeendpoints.pulse()


def clear_api_keys():
    gemini_ops = root.findChildren(tags=["gemini"])
    for each in gemini_ops:
        each.unstore("endpoints")


def BuildOps():
    clear_api_keys()
    set_defaults()
    clear_output_buffers()
    clear_storage()
    op("base_save_for_release").par.Package.pulse()
