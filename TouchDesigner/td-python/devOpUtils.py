import opDefaults


def clear_endpoints(targetOp: OP):
    try:
        targetOp.par.Apiendpoint.menuNames = []
        targetOp.par.Apiendpoint.menuLabels = []
    except Exception as e:
        pass


def set_defaults():
    # loop through each operator
    for each_op, pars_dict in opDefaults.defaults.items():

        # loop though defaults
        for each_par, value in pars_dict.items():
            # set default
            print(each_par, value)
            print(each_op.par[each_par])
            each_op.par[each_par].default = value
            # set par to default value
            each_op.par[each_par] = value

        clear_endpoints(each_op)


def clear_output_buffers():
    opDefaults.txtToTxt.op("text_output_buffer").clear()
    opDefaults.txtToChat.par.Clearchathistory.pulse()
    opDefaults.imgToTxt.op("text_output_buffer").clear()
    opDefaults.audioToTxt.op("text_output_buffer").clear()


def clear_storage():
    opDefaults.txtToTxt.op("text_output_buffer").unstore("metadata")

    opDefaults.txtToChat.op("fifo1").unstore("metadata")

    opDefaults.imgToTxt.op("text_output_buffer").unstore("metadata")

    opDefaults.txtToImg.op("script1").unstore("image_data")
    opDefaults.txtToImg.op("script1").unstore("metadata")

    opDefaults.imgToImg.op("script1").unstore("image_data")
    opDefaults.imgToImg.op("script1").unstore("metadata")

    op(opDefaults.audioToTxt).op("text_output_buffer").unstore("metadata")


def clear_vfs():
    opDefaults.txtToAudio.par.Deleteaudiofile.pulse()
    opDefaults.txtToSpeech.par.Deleteaudiofile.pulse()


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
    clear_vfs()
    op("base_save_for_release").par.Package.pulse()


def QuitProject():
    clear_output_buffers()
    clear_storage()
    clear_api_keys()
    clear_vfs()
    project.quit(force=True)
