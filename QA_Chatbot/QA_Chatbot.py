##Q&A Chatbot
from langchain.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os


## function to load OpenAI model and get response
def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"),temperature = 0.5)
    
    response=llm(question)
    return response

##initialize our streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

input = st.text_input("Input: ",key="input")
response=get_openai_response(input)

submit=st.button("Ask the question")

##if ask button is clicked
if submit:
    st.subheader("The Response is")
    st.write(response)
