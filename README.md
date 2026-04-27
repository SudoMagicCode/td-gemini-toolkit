# TouchDesigner Gemini Toolkit

*Development of the open source TouchDesigner Gemini Toolkit was supported by [UCLA REMAP](https://remap.ucla.edu/) and the [UCLA School of Theater, Film, and Television](https://www.tft.ucla.edu/), as part of the [2026 AI + Live Arts Hackathon.](https://datax.ucla.edu/news-events/events/ai-onstage-ai-live-arts-hackathon)*

## About this Project

* Built with TouchDesigner 2025.32460
* Works on : Windows 11, MacOS

Here you'll find a collection of custom TouchDesigner Components that use the Google Gemini API. Focused on an library independent workflow, this set of components is a batteries included collection that requires no additional libraries or dependencies to get working. The development of these components has focused on using non-blocking procedures in TouchDesigner to ensure there are no external library dependencies and that your project doesn't unexpectedly freeze. Development has focused on allowing for the use of multiple API keys across both studio and enterprise endpoints.

If you're just getting started and setting up a rapid prototype, then using an AI Studio API key is likely the fastest and easiest pathway for testing your ideas. If you're standing up a long running installation, you likely need the stability and pricing structure from Google Cloud's Vertex solution. This project handles both of these cases and provides some utility components, include an API Key Manager that makes it easy to centrally organize your Keys, and distribute them to all of the components in your project.

## Setup

### Download the `package.zip`

The TouchDesigner Gemini Toolkit is built on the principle that you want to get working quickly. For that reason you should get started by downloading the latest release of `tox` files [from the releases page](https://github.com/SudoMagicCode/td-gemini-toolkit/releases). Navigate to the latest release, click on `show all assets` and download the `package.zip` file. This file contains all of the single `tox` files packaged into a single library you can download.

### Drag and Drop

Get started using the Gemini Toolkit by dragging and dropping the `tox` files into your TouchDesigner projects. We recommend first adding  the `api_key_manager` to your project. Here you can add both Studio and Enterprise API keys for the respective Google AI platforms. By adding the [`api_key_manager`](https://sudomagiccode.github.io/td-gemini-toolkit/gemini-comps/gemini-ops/key-manager) first, every component you add after will pull credentials from the manager making it easy to work quickly in your project.

API Keys are kept in the storage of your operators. The [`api_key_manager`](https://sudomagiccode.github.io/td-gemini-toolkit/gemini-comps/gemini-ops/key-manager) has several convenience mechanics for both distributing and clearing keys from your project.

Next add any of the model components to your project:

| tox | description |
| --- | --- |
| txt_input | a prompt editing utility component |
| audio_to_txt | used for generating audio from text prompts |
| txt_to_audio | used for transcribing or describing audio as text. |
| txt_to_speech | used for generating speech audio from text |
| img_to_img | used for creating images from image and text prompts |
| img_to_txt | used for creating images from text prompts |
| txt_to_txt | used for working with text to text workflows |
| txt_to_chat | a chat style interaction tool for Gemini |
| txt_to_img | used from generating images from text |
| txt_to_vid | used for generating video from text |
| img_to_vid | used for generating videos from text and images |

Each component comes with a default prompt, inputs, outputs, and utility handles for making it easy to work with the Gemini API.

[Complete project documentation here](hhttps://sudomagiccode.github.io/td-gemini-toolkit/).

## Development

### Dependencies

* [TouchDesigner](https://derivative.ca/download)
* [Taskfile](https://taskfile.dev/)
* [Github CLI](https://cli.github.com/)
* Gemini API Access

## Gemini API Reference

[AI Studio](https://ai.google.dev/gemini-api/docs)
[Vertext AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start)

![<>](https://remap-ucla-edu.exactdn.com/wp-content/uploads/2018/08/remaplogo-New-Line-Break-760x180.png?strip=all)
