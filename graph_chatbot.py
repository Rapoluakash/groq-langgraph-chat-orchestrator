# graph_chatbot.py

from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict
from typing import Annotated

# 🔑 Set your Groq API key
GROQ_API_KEY = "your_groq_api_key_here"

# ✅ Initialize LLM
llm = ChatGroq(api_key=GROQ_API_KEY, model_name="llama3-8b-8192")

# 📦 Define the state structure
class State(TypedDict):
    messages: Annotated[list, add_messages]

# 💬 Define chatbot logic
def chatbot(state: State) -> State:
    return {"messages": llm.invoke(state["messages"])}

# 🧠 Build LangGraph
graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

# ✅ Required trigger (fixes 'No event triggers defined in `on`')
graph_builder.on("chatbot", lambda state: END)

# 🔁 Compile graph
graph = graph_builder.compile()

# 💬 Run chatbot loop
if __name__ == "__main__":
    print("🤖 LangGraph Chatbot Ready (Graph 1)")
    print("Type 'q' or 'quit' to exit.\n")

    while True:
        user_input = input("User: ")
        if user_input.lower() in ["q", "quit"]:
            print("Goodbye! 👋")
            break

        for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
            for value in event.values():
                if "messages" in value:
                    for msg in value["messages"]:
                        if hasattr(msg, "type") and msg.type == "ai":
                            print("Assistant:", msg.content)
