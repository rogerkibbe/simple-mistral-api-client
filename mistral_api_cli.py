import asyncio
import os
from dotenv import load_dotenv
from mistralai.async_client import MistralAsyncClient
from mistralai.models.chat_completion import ChatMessage


def get_model_choice(available_models):
    """Gets user input for model choice. Validate input"""
    num_models = len(available_models)
    while True:
        model_choice = input(
            f"Enter your choice (1-{num_models}) or press Enter for default ({num_models}): "
        ) or str(num_models)

        if model_choice.isdigit() and 1 <= int(model_choice) <= num_models:
            return available_models[int(model_choice) - 1]
        else:
            print(f"Please enter a number between 1 and {num_models}.")


def select_model():
    """Selects the model from .env or prompts user for choice."""
    model_name = os.getenv("MODEL")
    if not model_name:
        available_models = [
            ("Open Mistral 7B", "open-mistral-7b"),
            ("Open Mistral Mixtral-8x7B", "open-mixtral-8x7b"),
            ("Mistral Small", "mistral-small-latest"),
            ("Mistral Medium", "mistral-medium-latest"),
            ("Mistral Large", "mistral-large-latest")
        ]
        print("Please select the model you want to use:")
        for i, (friendly_name, _) in enumerate(available_models, start=1):
            print(f"{i}. {friendly_name}")

        friendly_name, model_name = get_model_choice(available_models)
        print(f"You are talking to {friendly_name}.\n")

    return model_name


async def main():
    load_dotenv()

    model_name = select_model()

    api_key = os.getenv("MISTRAL_API_KEY")
    while not api_key:
        api_key = input("Please enter your Mistral API key: ")

    client = MistralAsyncClient(api_key=api_key)

    messages = []

    while True:
        user_input = input("Enter your prompt (or type 'stop' to exit): ")
        if user_input == "stop":
            break

        messages.append(ChatMessage(role="user", content=user_input))

        try:
            response = client.chat_stream(model=model_name, messages=messages)

            combined_response = ""
            async for chunk in response:
                if chunk.choices[0].delta.content is not None:
                    chunk_content = chunk.choices[0].delta.content
                    combined_response += chunk_content
                    print(chunk_content, end="")

            messages.append(ChatMessage(role="assistant", content=combined_response))
            print("\n")
        except Exception as e:
            print(f"An error occurred: {e}")
            break

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
