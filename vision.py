from dotenv import load_dotenv
load_dotenv()  # loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Use the correct model name for image understanding
model = genai.GenerativeModel("gemini-2.5-flash-lite")

def get_gemini_response(input_text, image):
    if input_text != "":
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Application")

input_text = st.text_input("Input Prompt ", key="input")

uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    # Replaced use_column_width with use_container_width
    st.image(image, caption="Uploaded Image.", use_container_width=True)

submit = st.button("Tell me about the image")

## if submit is clicked
if submit:
    if image is None:
        st.error("Please upload an image first.")
    else:
        with st.spinner("Analyzing image..."):
            response = get_gemini_response(input_text, image)
            st.subheader("The Response is")
            st.write(response)