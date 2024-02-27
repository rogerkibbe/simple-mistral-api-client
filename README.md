<p align="Center">
  <img src="https://github-img.s3.amazonaws.com/mistral-ai-api.png">
  <br/>
  <h1 align="Center"> Mistral AI LLM Simple Chat Client - Command Line and Web</h1>
</p>

Note: This codebase is a weekend project e.g., it's a bit messy right now and will be cleaned up gradually

Mistral.AI offers an API with five LLM models:
1) Open Mistral 7B: Mistral 7B parameter model
2) Open Mistral Mixtral-8x7B: MOE Model
3) Mistral Small: Improved version of Open Mistral Mixtral-8x7B - API access only
4) Mistral Medium: Medium Size Model - API access only
5) Mistral Large: Largest model available - API access only

Whereas there are multiple ways to access the first two models (via various providers or by downloading the models from HuggingFace)
the only current way to run Mistral Small, Medium or Large is via their API.

The Python code in this project uses the Mistral API to let you access all five of the Mistral models via a chat interface.

There are two versions of a chat interface:
- `python mistral_api_cli.py`: Command line
- `python mistral_api_web.py`: Web GUI

## Prerequisites

Before running either Python script, make sure you have the following prerequisites:

1. Python 3.9 or higher.
2. `pip` for installing dependencies.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/rogerkibbe/simple-mistral-api-client
   cd simple-mistral-api-client
   ```

2. **Install Dependencies**
   - It's recommended to use a virtual environment:
     ```bash
     python -m venv mistralenv 
     source mistralenv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```
   - Install the required packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Environment Variables:**
   - Create a `.env` file in the project's root directory.
   - Obtain a Mistral API key from [MistralAI](https://mistral.ai/product/)
   - Add your Mistral API key to the `.env` file. Note: If the API key is not set in the `.env` file, the script will prompt you to enter it manually.)
     ```
     MISTRAL_API_KEY=your_api_key_here

## Running the Script

1. **Start the Script:**
   - Run the command line script using the command: `python mistral_api_cli.py`
   - Run the web script using the command: `panel serve mistral_api_web.py --show`

2. **Interacting with the command line version:**
   - Follow the on-screen prompts to select an AI model and start a conversation.
   - Type 'stop' to exit the chat client.

3. **Interacting with the Web version:**
   -  A browser window will automatically open. If needed, the URL will be shown in the terminal like this:
   - `Bokeh app running at: http://localhost:5006/mistral_api_web`
   - Choose the model and start your conversation
   - Feel free to change the model or parameters during your conversation
   - Quit the Python process to exit

## Troubleshooting

- Ensure that your Python version is 3.9 or higher.
- Check if the API key is correctly entered in the `.env` file. 
- If you encounter any issues or exceptions, please take a look at the error message for more details.


## API

- You can explore more of the Mistral API [here](https://docs.mistral.ai/api/) 

## Feedback

This was a fun weekend project to use Mistral's API. Feel free to make PRs or open issues if you have any suggestions.
Improvements and suggestions are always welcome!



