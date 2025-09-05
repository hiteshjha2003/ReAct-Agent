
# ReACT Framework Agent: Multi-Modal Reasoning with SERP & GEMINI Search Integration

<div align="center">
<p><strong>A ReACT-based Agent Framework leveraging SERP and GEMINI APIs for Knowledge-Augmented Reasoning</strong></p>
</div>

---

## 🚀 Overview

The **ReACT Framework Agent** is designed to enable **interactive reasoning and acting** over user queries by integrating **external search APIs**. It follows the **Reason+Act (ReACT)** paradigm, alternating between reasoning and performing actions to retrieve and synthesize knowledge.

### Key Features

**1. ReACT Agent Architecture**

* Implements the Reason+Act paradigm for iterative reasoning.
* Supports **multi-step reasoning**, allowing refinement of answers based on retrieved knowledge.

**2. Search Integration**

* **SERP API**: Provides real-time web search for factual information.
* **GEMINI API**: Enables structured searches for precise, curated results.

**3. Flexible Action Framework**

* Supports a variety of actions: web searches, knowledge extraction, API calls.
* Can integrate **custom tools** for dynamic decision-making.

**4. Extensible Design**

* Easily extendable to other APIs, retrieval systems, or custom reasoning modules.

---

## 🔍 Requirements

* **Python:** 3.10+
* **API Keys:**

  * SERP API Key (for web search)
  * GEMINI API Key (for structured search)

---

### Python Dependencies

```bash
# Create a virtual environment
conda create -n react-agent python=3.10
conda activate react-agent

# Install required dependencies
pip install -r requirements.txt
```

**Example dependencies may include:**
`requests`, `openai`, `python-dotenv`, `pandas`, `tiktoken`, etc.

---

## ⚙️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/hiteshjha2003/ReACT-Agent.git
cd ReACT-Agent
```

### 2. Configure API Keys

Create a `.env` file in the root directory:

```env
SERP_API_KEY=your_serp_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

### 3. Verify Dependencies

```bash
python check_dependencies.py
```

---

## 💻 Usage

### 1. Initialize the ReACT Agent

```python
from react_agent import ReACTAgent

# Initialize agent with API keys
agent = ReACTAgent(
    serp_api_key="YOUR_SERP_API_KEY",
    gemini_api_key="YOUR_GEMINI_API_KEY"
)
```

---

### 2. Perform Queries

```python
# Example query
query = "Who won the 2024 Formula 1 World Championship?"
response = agent.run(query)
print(response)
```

**Agent Workflow:**

1. Reason about the query.
2. Decide whether to perform a **SERP** or **GEMINI** search.
3. Collect relevant information from external sources.
4. Generate a **final answer** based on retrieved knowledge.

---

### 3. Advanced Options

**Multi-Step Reasoning**

```python
response = agent.run(query, max_steps=3)
```

**Custom Action Hooks**

You can define custom actions for the agent to use during reasoning:

```python
def my_custom_action(query):
    # Example: call another API or tool
    return "Custom action result"

agent.register_action("custom_search", my_custom_action)
```

---

## 📝 Best Practices

* Keep API keys secure; **never commit them to GitHub**.
* Limit search API usage to **avoid exceeding quotas**.
* For multi-turn reasoning, set a **maximum step count** to prevent infinite loops.
* Cache search results locally to **improve efficiency** for repeated queries.

---

## 🔧 Evaluation

* Test the agent on sample queries in `examples/test_queries.py`.
* Compare outputs against **ground truth** for factual accuracy.
* Enable debug mode to **log reasoning steps**:

```python
response = agent.run(query, debug=True)
```

---
Perfect! I can outline a **visual diagram for the ReACT Framework Agent** that shows the **flow of reasoning, actions, and search integration**. Here's a textual version you can later render with tools like **Mermaid, draw\.io, or Graphviz**. I’ll also provide a ready-to-use **Mermaid code** so you can include it directly in your README or Markdown.

---

### **Diagram Concept: ReACT Agent Flow**

**Flow:**

```
User Query
     │
     ▼
  [ReACT Agent]
     │
     ├──> Reasoning Step 1
     │       │
     │       ├──> Decide Action
     │       │        ├── SERP Search API
     │       │        │      └── Retrieve Web Results
     │       │        └── GEMINI API
     │       │               └── Retrieve Structured Results
     │       │
     │       └──> Integrate Retrieved Knowledge
     │
     ├──> Reasoning Step 2 (Optional Multi-Step)
     │
     ▼
 Final Answer Generation
     │
     ▼
 User Response
```

---

### **Mermaid Diagram Code**

```mermaid
flowchart TD
    A[User Query] --> B[ReACT Agent]
    B --> C1[Reasoning Step 1]
    C1 --> D1[Decide Action]
    D1 --> E1[SERP Search API]
    D1 --> E2[GEMINI API]
    E1 --> F1[Retrieve Web Results]
    E2 --> F2[Retrieve Structured Results]
    F1 --> G1[Integrate Retrieved Knowledge]
    F2 --> G1
    G1 --> C2[Reasoning Step 2 (Optional)]
    C2 --> H[Final Answer Generation]
    H --> I[User Response]
```

---

## 🙏 Acknowledgements

This framework builds upon:

* **ReACT**: Synergizing Reasoning and Acting in Language Agents ([arXiv](https://arxiv.org/abs/2210.03629))
* **SERP API**: Real-time web search integration
* **GEMINI API**: Structured knowledge retrieval

