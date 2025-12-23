# google-setup-adk

Basic Google ADK (Agent Development Kit) setup following the official documentation at [https://google.github.io/adk-docs/get-started/python/#installation](https://google.github.io/adk-docs/get-started/python/#installation)

## Prerequisites

- Python 3.10 or higher
- pip (Python package installer)

## Installation

1. **Create and activate a virtual environment** (recommended):

   ```bash
   python -m venv .venv
   ```

   Activate your virtual environment:
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows CMD:
     ```
     .venv\Scripts\activate.bat
     ```
   - On Windows PowerShell:
     ```
     .venv\Scripts\Activate.ps1
     ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**:

   - Get a Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and replace `your_api_key_here` with your actual API key

## Project Structure

```
.
├── agent.py           # Main agent logic with Gemini model
├── __init__.py        # Package initialization
├── .env.example       # Template for environment variables
├── .env               # Your actual API keys (not committed)
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

## Usage

Once installed, you can run the agent using the ADK CLI:

```bash
# Run the agent in interactive mode
adk run .

# Or launch the web UI
adk web --port 8000
```

## Agent Details

The default agent (`root_agent` in `agent.py`) is configured with:
- **Model**: `gemini-2.0-flash`
- **Purpose**: A helpful assistant that can answer questions and provide information
- **Tools**: Includes a sample `get_current_time` function as an example tool

You can customize the agent by editing `agent.py` to:
- Change the model
- Modify the instruction prompt
- Add new tools (Python functions)
- Adjust the agent's behavior

## Learn More

- [Google ADK Documentation](https://google.github.io/adk-docs/)
- [Google ADK Python Guide](https://google.github.io/adk-docs/get-started/python/)
- [Google ADK Samples](https://github.com/google/adk-samples)
