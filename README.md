# TD Gemini Ops

*Thank you to UCLA for funding the initial development of this open source project.*

## About this Project

* Built with TouchDesigner 2025.32460
* Works on : Windows11, MacOS

Here you'll find a collection of custom TouchDesigner Components that use the Google Gemini API. Focused on an library independent workflow, this set of components is a batteries included collection that requires no additional libraries or dependencies to get working. The development of these components has focused on using non-blocking procedures in TouchDesigner to ensure there are no external library dependencies and that your project doesn't unexpectedly freeze. Development has focused on allowing for the use of multiple API keys across both studio and enterprise endpoints.

If you're just getting started and setting up a rapid prototype, then using an AI Studio API key is likely the fastest and easiest pathway for testing your ideas. If you're standing up a long running installation, you likely need the stability and pricing structure from Google Cloud's Vertex solution. This project handles both of these cases and provides some utility components, include an API Key Manager that makes it easy to centrally organize your Keys, and distribute them to all of the components in your project.

## Working with the Components

[Complete project documentation here](https://sudomagiccode.github.io/td-gemini-tools/).

## Development

### Dependencies

* [TouchDesigner](https://derivative.ca/download)
* [Taskfile](https://taskfile.dev/)
* [Github CLI](https://cli.github.com/)
* Gemini API Access

## Gemini API Reference

[AI Studio](https://ai.google.dev/gemini-api/docs)
[Vertext AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start)
