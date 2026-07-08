import os
from dotenv import load_dotenv
import streamlit as st

# LangChain imports
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

# Load environment variables from .env
load_dotenv()

# Enable LangSmith tracing if you want logs in your dashboard
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),
        ("user", "Question: {question}")
    ]
)

# Streamlit UI
st.title("LangChain Demo With LLAMA2 API")
input_text = st.text_input("Search the topic you want")

if input_text:
    # Initialize model (example with Ollama for local LLaMA2, or ChatOpenAI for OpenAI models)
    llm = Ollama(model="llama2")  # if you have Ollama running locally
    # llm = ChatOpenAI(model="gpt-4o-mini")  # if using OpenAI

    chain = prompt | llm | StrOutputParser()
    response = chain.invoke({"question": input_text})

    st.write("### Response")
    st.write(response)

# ollama LLAma2 LLm 
llm=Ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))