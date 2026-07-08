import requests
import streamlit as st

def get_essay_response(input_text):
    response = requests.post(
        "http://localhost:8000/essay/invoke",
        json={"input": {"topic": input_text}}
    )
    data = response.json()
    output = data.get("output")
    # Handle both dict and string cases
    if isinstance(output, dict):
        return output.get("content", "No content returned")
    return output

def get_poem_response(input_text):
    response = requests.post(
        "http://localhost:8000/poem/invoke",
        json={"input": {"topic": input_text}}
    )
    data = response.json()
    return data.get("output", "No output returned")

# Streamlit UI
st.title("Langchain Demo With LLAMA2 API")

input_text = st.text_input("Write an essay on")
input_text1 = st.text_input("Write a poem on")

if input_text:
    st.write(get_essay_response(input_text))

if input_text1:
    st.write(get_poem_response(input_text1))
