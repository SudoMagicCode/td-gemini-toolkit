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

`base_text_to_text`

### base_text_to_chat

### base_text_to_img

### base_img_to_text

### base_img_and_text_to_image

### base_text_to_video

### base_image_to_video

### base_text_and_img_to_video

### base_text_to_audio

### base_audio_to_text

### base_text_and_audio_to_audio
