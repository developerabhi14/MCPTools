from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

import asyncio

async def main():
    client=MultiServerMCPClient(
        {
            'calculator':{
                'command':"python",
                "args":["calculator.py"],
                'transport':'stdio',
            },
            'filesearch':{
                'url':'http://localhost:8000/mcp',
                'transport':'streamable_http'
            }
        }
    )

    tools=await client.get_tools()
    llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

    agent=create_react_agent(
        llm, tools
        )
    
    search_response=await agent.ainvoke(
        {"messages":[{'role':"user","content":"Find me all the notes that is related to machine learning"}]}
    )
    print(search_response)
    print("\n\n")
    print("MathsResponse:",search_response['messages'][-1].content)

asyncio.run(main())