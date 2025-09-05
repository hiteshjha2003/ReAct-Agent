import streamlit as st
from dotenv import load_dotenv
import os 
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.react.agent import Agent
from src.react.enums import Name
from src.tools.serp import search_google
from src.tools.wiki import search_wikipedia

print("Imported Sucessfully")

import asyncio 
try:
    loop = asyncio.get_event_loop()
except RuntimeError as e:
    if "There is no current event loop" in str(e):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)


load_dotenv()

st.set_page_config(page_title="ReACT Gemini Agentic System", layout="wide")
st.title("REACT Agent with Gemini")

query = st.text_input("Enter you Question:", "")

if query:
    agent = Agent(api_key=os.getenv("GEMINI_API_KEY"))
    agent.register(Name.GOOGLE, search_google)
    agent.register(Name.WIKIPEDIA ,search_wikipedia)

    with st.spinner("Thinking...."):
        history = agent.execute(query)
    
    st.subheader("Agent Reasonining Log")
    st.text(history)
