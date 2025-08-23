from dotenv import load_dotenv
load_dotenv() #loading all the environment variables
 
import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## fucntion to load Gemini Pro Model and get response

model = genai.GenerativeModel("gemini-1.5-flash")
def get_gemini_reponse(question):
  response = model.generate_content(question) 
  return response.text

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

input=st.text_input("Input: ",key="input")
submit=st.button("Ask The Question")

# when submit is click

if submit:
  response=get_gemini_reponse(input)
  st.subheader("The Response is")
  st.write(response)   