apiKeyManager = op("base_comps/base_api_key_manager")
txtToTxt = "base_comps/base_txt_to_txt"
txtToChat = "base_comps/base_txt_to_chat"
imgToTxt = "base_comps/base_img_to_txt"
txtToImg = "base_comps/base_txt_to_img"
imgToImg = "base_comps/base_img_to_img"
txtTovVid = "base_comps/base_txt_to_vid"
imgToVid = "base_comps/base_img_to_vid"
audioToTxt = "base_comps/base_audio_to_txt"
txtToAudio = "base_comps/base_txt_to_audio"
txtToSpeech = "base_comps/base_txt_to_speech"


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
    txtTovVid: {
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
