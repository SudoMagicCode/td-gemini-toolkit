# TD Gemini Ops

*Thank you to UCLA for funding the initial development of this open source project.*

Here you'll find a collection of custom TouchDesigner Components that use the Google Gemini API. Focused on an library independent workflow, this set of components is a batteries included collection that requires no additional libraries or dependencies to get working.

## Common Controls and Parameters

### API Settings Page

Parameter Name | Parameter | Type | Description |
--- | --- | --- | --- |
Has API Key | `Hasapikey` | Toggle | *(Read Only)* Indicator for if this COMP has an API Key set to use with Gemini API |
Add API Key | `Addapikey` | Pulse | Adds an API key to this COMP |
Distribute API Key | `Distributeapikey` | Pulse | Distributes the API key from this COMP to all other gemini COMPs |
Clear API Key | `Clearapikey` | Pulse | Clears this COMP's API key |

### Gemini Page - Avialable on all Components

Parameter Name | Parameter | Type | Description |
--- | --- | --- | --- |
Generating | `Generating` | Toggle | *(Read Only)* Indicator for if this COMP is currently waiting on a response from the Gemini API |
Request ID | `Requestid` | Int | *(Read Only)* Used for tracking the current request for this COMP |
Auto Generate | `Autogenerate` | Toggle | Toggle on to automatically submit request when the text input changes |
Generate | `Generate` | Pulse | Manually start generation process |
Cancel | `Cancel` | Pulse | Cancel the currently running request |

## Tools Inventory

### Text to Text

TOX name `base_text_to_text`

Summary

A TouchDesigner component for generating synthetic text with the Google Gemini API based on an input prompt. The first input to this component should be a `Text DAT` - the contents of this `DAT` will be used as the prompt for generating text.

Controls

Parameter Name | Parameter | Type | Description |
--- | --- | --- | --- |
Default Prompt | `Defaultprompt` | String | The prompt used when no input `Text DAT` is connected |
Model | `Model` | Menu | The Gemini Model to use for processing this text prompt |

Outputs

Output Index | Name | Type | Description |
--- | --- | --- | --- |
0 | `out_response` | `DAT` | Contains the response back from the Google Gemini API |
1 | `out_metadata` | `DAT` | Contains the metadata back from the Google Gemini API, this includes data like total token count, and prompt token count |

### Text Chat

TOX name `base_text_to_chat`

Summary

A TouchDesigner component for generating synthetic text with the Google Gemini API based on a chat style exchange. The first input to the Component is used as the input text for the model. The second input can be used to provide a chat history, or context, when interacting with the model.

Controls

Parameter Name | Parameter | Type | Description |
--- | --- | --- | --- |
Prompt | `Prompt` | String | The prompt used when no input `Text DAT` is connected |
Clear Length | `Chatlength` | int | The number length of the chat history |
Clear Chat History | `Clearchathistory` | Pulse | Clears the chat history |

Outputs

Output Index | Name | Type | Description |
--- | --- | --- | --- |
0 | `out_chat` | `DAT` | Contains the response back from the Google Gemini API as a series of rows that contain both the user and model exchange |
1 | `out_chat_as_block` | `DAT` | A single text block formatted as a chat history |
2 | `out_metadata` | `DAT` | Contains the metadata back from the Google Gemini API, this includes data like total token count, and prompt token count |

### Text to Image

TOX name `base_text_to_img`

Summary
A TouchDesigner component for generating synthetic images with the Google Gemini API.

Controls

Parameter Name | Parameter | Type | Description |
--- | --- | --- | --- |
Default Prompt | `Defaultprompt` | String | The prompt used when no input `Text DAT` is connected |
Resolution | `Resolution` | Menu | The output image resolution |
Aspect Ratio | `Aspectratio` | Menu | The output image aspect ratio |

Outputs

Output Index | Name | Type | Description |
--- | --- | --- | --- |
0 | `out_response` | `TOP` | The image output from the Google Gemini API |
1 | `out_metadata` | `DAT` | Contains the metadata back from the Google Gemini API, this includes data like total token count, and prompt token count |

### Image to Text

TOX name `base_img_to_text`

Summary
A TouchDesigner component for generating synthetic text from an image and a prompt with the Google Gemini API.

Controls

Parameter Name | Parameter | Type | Description |
--- | --- | --- | --- |
Input Resolution | `Inputresolution` | Menu | Downscale options for reducing the image resolution - reducing your input resolution by a half or quarter will help maintain high performance |
Default Prompt | `Defaultprompt` | String | The prompt used when no input `Text DAT` is connected |
Aspect Ratio | `Aspectratio` | Menu | The output image aspect ratio |

Outputs

Output Index | Name | Type | Description |
--- | --- | --- | --- |
0 | `out_response` | `DAT` | Contains the response back from the Google Gemini API |
1 | `out_metadata` | `DAT` | Contains the metadata back from the Google Gemini API, this includes data like total token count, and prompt token count |

### Image and Text to Image

TOX name `base_img_and_text_to_image`

Summary
A TouchDesigner component for generating synthetic images from image and text inputs with the Google Gemini API.

Controls

Parameter Name | Parameter | Type | Description |
--- | --- | --- | --- |
Input Resolution | `Inputresolution` | Menu | Downscale options for reducing the image resolution - reducing your input resolution by a half or quarter will help maintain high performance |
Use Input | `Useinput` | Toggle | When on, uses the resolution and aspect ratio of the input image. When off, allows for overriding the resolution and aspect ratio |
Resolution | `Resolution` | Menu | The output image resolution |
Aspect Ratio | `Aspectratio` | Menu | The output image aspect ratio |
Default Prompt | `Defaultprompt` | String | The prompt used when no input `Text DAT` is connected |

Outputs

Output Index | Name | Type | Description |
--- | --- | --- | --- |
0 | `out_response` | `TOP` | The image output from the Google Gemini API |
1 | `out_metadata` | `DAT` | Contains the metadata back from the Google Gemini API, this includes data like total token count, and prompt token count |

### Text to Video

TOX name `base_text_to_video`

Summary
A TouchDesigner component for generating synthetic video with the Google Gemini API.

Controls

Parameter Name | Parameter | Type | Description |
--- | --- | --- | --- |
Default Prompt | `Defaultprompt` | String | The prompt used when no input `Text DAT` is connected |
Model | `Model` | Menu | The Gemini Model to use for processing this text prompt |
Resolution | `Resolution` | Menu | The output image resolution |
Aspect Ratio | `Aspectratio` | Menu | The output image aspect ratio |
Video Length | `Videolength` | Menu | The duration of the output video |

Output Index | Name | Type | Description |
--- | --- | --- | --- |
0 | `out_response` | `TOP` | The video output from the Google Gemini API |
1 | `out_response_audio` | `CHOP` | The video audio output from the Google Gemini API |
2 | `out_remote_path` | `DAT` | A table which contains the link to the remote asset generated by the Gemini API|

### Image to Video

TOX name `base_image_to_video`

Summary

Controls

Parameter Name | Parameter | Type | Description |
--- | --- | --- | --- |
Default Prompt | `Defaultprompt` | String | The prompt used when no input `Text DAT` is connected |
Model | `Model` | Menu | The Gemini Model to use for processing this text prompt |
Resolution | `Resolution` | Menu | The output image resolution |
Aspect Ratio | `Aspectratio` | Menu | The output image aspect ratio |
Video Length | `Videolength` | Menu | The duration of the output video |

Output Index | Name | Type | Description |
--- | --- | --- | --- |
0 | `out_response` | `TOP` | The video output from the Google Gemini API |
1 | `out_response_audio` | `CHOP` | The video audio output from the Google Gemini API |
2 | `out_remote_path` | `DAT` | A table which contains the link to the remote asset generated by the Gemini API|

### Text to Audio

TOX name `base_text_to_audio`

Summary

Controls

Parameter Name | Parameter | Type | Description |
--- | --- | --- | --- |
Place Holder | `Placeholder` | int | about |

### Audio to Text

TOX name `base_audio_to_text`

Summary

Controls

Parameter Name | Parameter | Type | Description |
--- | --- | --- | --- |
Place Holder | `Placeholder` | int | about |

### base_text_and_audio_to_audio

TOX name `base_text_and_audio_to_audio`

Summary

Controls

Parameter Name | Parameter | Type | Description |
--- | --- | --- | --- |
Place Holder | `Placeholder` | int | about |
