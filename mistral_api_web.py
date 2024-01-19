import os
import sys
from dotenv import load_dotenv
import panel as pn
from mistralai.async_client import MistralAsyncClient
from mistralai.models.chat_completion import ChatMessage

pn.extension()

load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")

# Stop if no API key
if not api_key:
    print("Error: MISTRAL_API_KEY is not defined. Please set the API key in your environment.")
    sys.exit()  # Exit the script

client = MistralAsyncClient(api_key=api_key)

# available models
available_models = [
    ("Mistral 7B", "mistral-tiny"),
    ("Mistral Mixtral-8x7B", "mistral-small"),
    ("Mistral Medium", "mistral-medium"),
]

# message history for LLM
messages = []


# Create chat interface
def create_chat_interface(model_api_id, model_name):
    async def callback(contents: str, user: str, instance: pn.chat.ChatInterface):
        global messages
        messages.append(ChatMessage(role="user", content=contents))

        # Handle streaming
        accumulated_message = ""
        async for chunk in client.chat_stream(model=model_api_id, messages=messages):
            part = chunk.choices[0].delta.content
            if part is not None:
                accumulated_message += part
                yield accumulated_message

        messages.append(ChatMessage(role="assistant", content=accumulated_message))

    chat_interface = pn.chat.ChatInterface(callback=callback, callback_user=model_name)
    chat_interface.send(
        f"Chatting with {model_name}. Send a message to get a reply!", user="System", respond=False
    )
    return chat_interface


def on_model_selected(event):
    model_name = event.obj.name
    model_api_id = dict(available_models)[model_name]
    chat_view = create_chat_interface(model_api_id, model_name)
    main_view.objects = [chat_view]

alert = pn.pane.Alert("", alert_type="light", visible=False)

# Create buttons for model selection
model_buttons = [pn.widgets.Button(name=model_name, button_type='primary') for model_name, _ in available_models]
for button in model_buttons:
    button.on_click(on_model_selected)

# Title and Model Selection Message
title = pn.pane.Markdown("## Mistral API Chat App - [GitHub](https://github.com/rogerkibbe)")
model_selection_message = pn.pane.Markdown("### Select your Mistral Model")

# Model selection layout
model_selection_layout = pn.Column(alert, model_selection_message, *model_buttons, sizing_mode='stretch_width')

# Main view initially showing model selection
main_view = pn.Column(title, model_selection_layout, sizing_mode='stretch_width')

main_view.servable()
