ReACT Framework Agent: Multi-Modal Reasoning with SERP & GEMINI Search Integration
<div align="center"> <p><strong>A ReACT-based Agent Framework leveraging SERP and GEMINI APIs for Knowledge-Augmented Reasoning</strong></p> </div>
🚀 Overview

The ReACT Framework Agent is designed to enable interactive reasoning and acting over queries by integrating external search APIs.

Key Features:

ReACT Agent Architecture

Implements the Reason+Act (ReACT) paradigm where the agent alternates between reasoning and performing actions.

Supports multi-step reasoning, allowing iterative refinement of answers based on retrieved knowledge.

Search Integration

SERP API: Enables real-time search over web data for factual knowledge retrieval.

GEMINI API: Provides additional search capabilities with advanced structured results.

Flexible Action Framework

Actions can include web searches, knowledge extraction, or API queries.

Supports tool integration for dynamic decision-making.

Extensible Design

Can be extended to other APIs, retrieval systems, or custom reasoning modules.

🔍 Requirements

Python 3.10+

API Keys:

SERP API Key (for web search)

GEMINI API Key (for structured search)

Python Dependencies
# Create virtual environment
conda create -n react-agent python=3.10
conda activate react-agent

# Install dependencies
pip install -r requirements.txt


Example dependencies may include: requests, openai, python-dotenv, pandas, tiktoken, or other libraries your agent uses.

⚙️ Setup

Clone the repository

git clone https://github.com/hiteshjha2003/ReACT-Agent.git
cd ReACT-Agent


Add API Keys

Create a .env file in the root directory:

SERP_API_KEY=your_serp_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here


Verify Dependencies

python check_dependencies.py

💻 Usage
1. Initialize the ReACT Agent
from react_agent import ReACTAgent

# Initialize agent with API keys
agent = ReACTAgent(
    serp_api_key="YOUR_SERP_API_KEY",
    gemini_api_key="YOUR_GEMINI_API_KEY"
)

2. Perform Queries
# Run a query using the agent
query = "Who won the 2024 Formula 1 World Championship?"
response = agent.run(query)
print(response)


The agent will:

Reason about the query.

Decide whether to perform a SERP search or GEMINI search.

Collect relevant information from external sources.

Generate a final answer based on retrieved knowledge.

3. Advanced Options

Multi-Step Reasoning:

response = agent.run(query, max_steps=3)


Custom Action Hooks:

You can define custom actions for the agent to use during reasoning:

def my_custom_action(query):
    # Example: call another API or tool
    return "Custom action result"

agent.register_action("custom_search", my_custom_action)

📝 Best Practices

Keep API keys secret; do not commit them to GitHub.

Limit search API usage to avoid exceeding quotas.

For multi-turn reasoning, consider setting a maximum step count to prevent infinite loops.

Cache search results locally to improve efficiency for repeated queries.

🔧 Evaluation

Test the agent on sample queries in examples/test_queries.py.

Compare outputs with ground truth for factual accuracy.

Log agent reasoning steps for debugging:

response = agent.run(query, debug=True)

🙏 Acknowledgements

This framework builds upon:

ReACT: Synergizing Reasoning and Acting in Language Agents

SERP API for real-time web search

GEMINI API for structured search integration
