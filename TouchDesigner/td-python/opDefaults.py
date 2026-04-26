apiKeyManager = op("/base_root/base_project/base_comps/base_api_key_manager")
txtToTxt = op("/base_root/base_project/base_comps/base_txt_to_txt")
txtToChat = op("/base_root/base_project/base_comps/base_txt_to_chat")
imgToTxt = op("/base_root/base_project/base_comps/base_img_to_txt")
txtToImg = op("/base_root/base_project/base_comps/base_txt_to_img")
imgToImg = op("/base_root/base_project/base_comps/base_img_to_img")
txtToVid = op("/base_root/base_project/base_comps/base_txt_to_vid")
imgToVid = op("/base_root/base_project/base_comps/base_img_to_vid")
audioToTxt = op("/base_root/base_project/base_comps/base_audio_to_txt")
txtToAudio = op("/base_root/base_project/base_comps/base_txt_to_audio")
txtToSpeech = op("/base_root/base_project/base_comps/base_txt_to_speech")

opBuilder = op("/base_root/base_project/base_save_for_release")

defaults = {
    apiKeyManager: {
        "Selectedviewer": "icon",
    },
    txtToTxt: {
        "Requestid": 0,
        "Generating": False,
        "Hasapikey": False,
        "Selectedviewer": "icon",
        "Callbacksdat": "",
        "Defaultprompt": "Draft a one-sentence synthwave spell to optimize system logic and purge latency.",
        "Autogenerate": False,
    },
    txtToChat: {
        "Requestid": 0,
        "Generating": False,
        "Hasapikey": False,
        "Selectedviewer": "icon",
        "Callbacksdat": "",
        "Defaultprompt": "In a couple sentences, explain how quartz timing serves as the fundamental ritual for computing precision. Include a citation.",
        "Autogenerate": False,
    },
    imgToTxt: {
        "Requestid": 0,
        "Generating": False,
        "Hasapikey": False,
        "Selectedviewer": "icon",
        "Callbacksdat": "",
        "Defaultprompt": "Provide a one-sentence description, focusing on light, energy, or mechanical components.",
        "Autogenerate": False,
    },
    txtToImg: {
        "Requestid": 0,
        "Generating": False,
        "Hasapikey": False,
        "Selectedviewer": "icon",
        "Defaultprompt": "Generate a cinematic shot of a 1980s beige desktop computer pulsing with warm, protective neon magic.",
        "Autogenerate": False,
    },
    imgToImg: {
        "Requestid": 0,
        "Generating": False,
        "Hasapikey": False,
        "Selectedviewer": "icon",
        "Callbacksdat": "",
        "Defaultprompt": "Transform this image into a dreamlike 80s magazine landscape Do not include any words.",
        "Autogenerate": False,
    },
    txtToVid: {
        "Requestid": 0,
        "Generating": False,
        "Hasapikey": False,
        "Selectedviewer": "icon",
        "Callbacksdat": "",
        "Defaultprompt": "A arcane magical glyphs weaving through a 1980s-style grid landscape inside a retro-futuristic monitor.",
        "Autogenerate": False,
    },
    imgToVid: {
        "Requestid": 0,
        "Generating": False,
        "Hasapikey": False,
        "Selectedviewer": "icon",
        "Callbacksdat": "",
        "Defaultprompt": "Transform this image into a vaporwave neon timelapse. ",
        "Autogenerate": False,
    },
    audioToTxt: {
        "Requestid": 0,
        "Generating": False,
        "Hasapikey": False,
        "Selectedviewer": "icon",
        "Callbacksdat": "",
        "Tempfile": "",
        "Defaultprompt": "Transcribe this audio, include only the transcription in your response.",
        "Autogenerate": False,
    },
    txtToAudio: {
        "Requestid": 0,
        "Generating": False,
        "Hasapikey": False,
        "Selectedviewer": "icon",
        "Callbacksdat": "",
        "Defaultprompt": "Compose an 80s synthwave track with warm analog pads and a steady beat, representing the magic hum of a computer.",
        "Includeimage": False,
        "Autogenerate": False,
    },
    txtToSpeech: {
        "Requestid": 0,
        "Generating": False,
        "Hasapikey": False,
        "Selectedviewer": "icon",
        "Callbacksdat": "",
        "Defaultprompt": "[neutral] The quartz crystal drives the system clock. It triggers the logic gates and commands  data flow. [cheerfully] Timing is everything!",
        "Autogenerate": False,
    },
}
