# simple-mistral-api-client
# MistralAI Chat Client

This Python script enables you to interact with various MistralAI models using a chat client. It allows you to select different AI models and send prompts to them, receiving AI-generated responses.

## Prerequisites

Before running the script, make sure you have the following prerequisites:

1. Python 3.7 or higher.
2. `pip` for installing dependencies.

## Installation

1. **Clone the Repository:**
   - Clone this repository to your local machine using `git clone`.

2. **Install Dependencies:**
   - Run `pip install -r requirements.txt` to install the required Python packages.

## Setup

1. **Environment Variables:**
   - Create a `.env` file in the root directory of the project.
   - Add your Mistral API key to the `.env` file:
     ```
     MISTRAL_API_KEY=your_api_key_here
     ```
   - Optionally, you can specify the default model in the `.env` file:
     ```
     MODEL=mistral-tiny
     ```

2. **API Key:**
   - Obtain an API key from MistralAI.
   - If the API key is not set in the `.env` file, the script will prompt you to enter it manually.

## Running the Script

1. **Start the Script:**
   - Run the script using the command: `python script_name.py`.
   - Replace `script_name.py` with the actual name of the script.

2. **Interacting with the AI:**
   - Follow the on-screen prompts to select an AI model (if not set in `.env`) and enter your queries.
   - Type 'stop' to exit the chat client.

## Troubleshooting

- Ensure that your Python version is 3.7 or higher.
- Check if the API key is correctly entered in the `.env` file or provided when prompted.
- If you encounter any issues or exceptions, please refer to the error message for more details.

## License

Specify your license details here.

# MistralAI Chat Application

This application provides a graphical chat interface using the Panel library to interact with various MistralAI models. It allows users to select a model and engage in a conversation with the AI.

## Prerequisites

Before running this application, you will need:

1. Python 3.7 or higher.
2. `pip` for installing Python packages.

## Installation

1. **Clone the Repository:**
   - Clone this repository to your local machine using `git clone`.

2. **Install Dependencies:**
   - Run `pip install -r requirements.txt` to install the necessary Python packages.
   - Ensure that Panel and other required libraries are included in your `requirements.txt`.

## Setup

1. **Environment Variables:**
   - Create a `.env` file in the root directory of your project.
   - Add your Mistral API key:
     ```
     MISTRAL_API_KEY=your_api_key_here
     ```

2. **Obtain API Key:**
   - Get an API key from MistralAI and set it in the `.env` file.
   - The application will not run without a valid API key.

## Running the Application

1. **Start the Application:**
   - Run the script using the command: `panel serve mistral_api_web.py `.
   - Go to the URL Panel creates

2. **Using the Interface:**
   - The Panel interface will open in your default web browser.
   - Select a Mistral model to start chatting.
   - Enter your messages in the chat interface to interact with the AI.

## Troubleshooting

- Make sure Python 3.7 or higher is installed.
- Check if the API key is correctly set in the `.env` file.
- Ensure all dependencies are installed via `pip`.

## License

Specify your license details here.

