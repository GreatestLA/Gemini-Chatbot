
"""
Gemini Chatbot - Simple, Fast, and Clean
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage, SystemMessage
from dotenv import load_dotenv
import os
import sys

load_dotenv()

@tool
def calculator(a: float, b: float) -> str:
    """Add two numbers together."""
    return f"{a + b}"
    
@tool
def say_hello(name: str) -> str:
    """Greet a user by name."""
    return f"Hello {name}!"

def main():
    
    if not os.getenv("GOOGLE_API_KEY"):
        print("❌ Error: GOOGLE_API_KEY not found in .env file")
        sys.exit(1)

   
    print("Starting chatbot...", end=" ", flush=True)
    
    models = ["gemini-2.0-flash-exp", "gemini-flash-latest", "gemini-2.0-flash"]
    llm = None
    
    for model in models:
        try:
            llm = ChatGoogleGenerativeAI(model=model, temperature=0.9)
            break
        except:
            continue
    
    if not llm:
        print("\n❌ Connection failed. Check your API key.")
        sys.exit(1)
    
    print("Ready!\n")
    
    
    tools = [calculator, say_hello]
    llm_with_tools = llm.bind_tools(tools)
    messages = [SystemMessage(content="You are a helpful AI assistant. Answer any questions naturally.")]
    
  
    print("Gemini Chatbot")
    print("Type 'quit' to exit\n")
    print("-" * 50)
    
    while True:
        try:
           
            user_input = input("\nYou: ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ["quit", "exit", "q"]:
                print("\nGoodbye!")
                break
            
           
            messages.append(HumanMessage(content=user_input))
            
            
            response = llm_with_tools.invoke(messages)
            messages.append(response)
            
           
            if response.tool_calls:
                for tool_call in response.tool_calls:
                    selected_tool = next((t for t in tools if t.name == tool_call["name"]), None)
                    
                    if selected_tool:
                        result = selected_tool.invoke(tool_call["args"])
                        messages.append(ToolMessage(content=str(result), tool_call_id=tool_call["id"]))
                
                final_response = llm_with_tools.invoke(messages)
                messages.append(final_response)
                print(f"\nAssistant: {final_response.content}")
            else:
                print(f"\nAssistant: {response.content}")
                
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)[:100]}")
            if messages:
                messages.pop()

if __name__ == "__main__":
    main()
