Summary

A TouchDesigner for manager API keys across your project. This component make sit easy to manage multiple API keys and distribute them to the gemini components you add to your project. A typical work flow would include first adding this component to your project, adding your API keys, and then adding any other gemini components to your project.

The API Key Manager is an operator that uses the global op shortcut geminiAPIKeyServer. This means you should only include one of these in any given TouchDesigner toe file. When a new gemini component is added they will first attempt to find this component by using it's global op shortcut, and then pull any endpoints that are stored in this key manager. Practically speaking, this means that when you add a new gemini component it will pull any API keys from this component so it's ready to make requests right away.

Help