# graph_chatbot.py

from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict
from typing import Annotated

# 🔐 Your Groq API key
GROQ_API_KEY = "your_groq_api_key_here"  # Replace this

# ✅ Initialize LLM with a valid model
llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model_name="llama3-8b-8192"  # Supported model
)

# 📦 Define the state structure
class State(TypedDict):
    messages: Annotated[list, add_messages]

# 💬 Chatbot logic
def chatbot(state: State) -> State:
    return {
        "messages": llm.invoke(state["messages"])
    }

# 🧠 Build the graph
graph_builder = StateGraph(State)

# ✅ Add chatbot node and edges
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

# ✅ REQUIRED: define event trigger
graph_builder.on("chatbot", lambda state: END)

# ✅ Compile the graph
graph = graph_builder.compile()

# 🔁 Interactive chat loop
if __name__ == "__main__":
    print("🤖 LangGraph Chatbot Ready! Type 'q' to quit.\n")

    while True:
        user_input = input("User: ")
        if user_input.lower() in ['q', 'quit']:
            print("👋 Goodbye! Thanks for using LangGraph Chatbot.")
            break

        for event in graph.stream({
            "messages": [{"role": "user", "content": user_input}]
        }):
            for value in event.values():
                if "messages" in value:
                    for msg in value["messages"]:
                        if hasattr(msg, "type") and msg.type == "ai":
                            print("Assistant:", msg.content)
