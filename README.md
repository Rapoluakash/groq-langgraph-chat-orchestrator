# groq-langgraph-chat-orchestrator

# 🤖 Groq LangGraph Chat Orchestrator

A modular, state-machine-driven chatbot built using [LangGraph](https://github.com/langchain-ai/langgraph), powered by ultra-fast [Groq LLMs](https://console.groq.com), and designed to explore how large language models can be orchestrated using graph-based control flows.

---

## 🚀 Features

- ✅ Powered by Groq's blazing-fast inference engine (e.g. `llama3-8b-8192`)
- ✅ Built with LangGraph — a stateful graph execution framework
- ✅ Clean separation of chatbot logic using typed graph states
- ✅ Real-time CLI chatbot interface
- ✅ Easily extendable to multi-node or multi-agent workflows

---

## 📂 Project Structure

```bash
groq-langgraph-chat-orchestrator/
├── graph1.ipynb           # Single-node LangGraph chatbot
├── graph2.ipynb           # Multi-node or routed example (optional)
├── graph_chatbot.py       # Clean Python script (CLI chatbot)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
````

---

## ⚙️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/groq-langgraph-chat-orchestrator.git
cd groq-langgraph-chat-orchestrator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> ✅ Requires Python 3.9–3.11

---

### 3. Set Your Groq API Key

Create a `.env` file or set it directly in your script:

```bash
export GROQ_API_KEY=your_groq_api_key
```

Or in Python:

```python
llm = ChatGroq(api_key="your_groq_api_key", model_name="llama3-8b-8192")
```

---

## ▶️ Run the Chatbot

```bash
python graph_chatbot.py
```

Then start chatting:

```text
User: Hello!
Assistant: Hi! How can I help you today?
```

---

## 🧠 Built With

* [LangGraph](https://github.com/langchain-ai/langgraph)
* [LangChain](https://github.com/langchain-ai/langchain)
* [Groq API](https://console.groq.com)
* Python 3.11

---

## 📜 License

MIT License © 2025 \[Rapolu Akash]

---

## 🌟 Star this repo if it helped you!

Feel free to fork and customize it for your own LLM apps.

```

---

Would you like me to also generate:
- `.env.example` file
- `graph2.py` version (multi-node flow)
- or `LICENSE` for open-source sharing?

Just say the word!
```
