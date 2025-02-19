# Flow-CrewAI

A Python project demonstrating the use of CrewAI for building intelligent workflow systems with LLM routing capabilities.

## Features

- Intelligent routing based on topics (medical, finance, sports)
- Integration with Gemini AI for content generation
- Flow visualization capabilities
- Modular and extensible architecture

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/flow-crewai.git
cd flow-crewai
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. Install the package in development mode:
```bash
uv pip install -e .
```

## Configuration

1. Create a `.env` file in the root directory
2. Add your Gemini API key:
```
GEMINI_API_KEY=your_api_key_here
```

## Usage

The project includes several example flows:

1. Router Flow:
```bash
uv run router_flow
```

2. Simple Flow:
```bash
uv run simple-flow
```

## Project Structure

```
flow-crewai/
├── src/
│   └── flow_crewai/
│       ├── __init__.py
│       ├── router_flow.py
│       └── simple_flow.py
├── .env
├── .gitignore
├── pyproject.toml
└── README.md
```

## Dependencies

- crewai >= 0.100.1
- litellm >= 1.59.8
- python-dotenv >= 1.0.1
- certifi >= 2024.2.2

## License

MIT License
