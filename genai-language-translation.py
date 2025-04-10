import getpass
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core. output_parsers import StrOutputParser

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getpass("Enter your google AI API key : ")


os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true" # To start the tracing make it true
os.environ["LANGCHAIN-API-KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Now we can instantiate our generate chat completions
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model = "gemini - 1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    
)