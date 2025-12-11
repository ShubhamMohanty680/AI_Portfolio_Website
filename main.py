import streamlit as st
import dotenv
import langchain
from langchain_google_genai import GoogleGenerativeAI,ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
import zipfile

import os
os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")

st.title("Portfolio Website Generator")

st.set_page_config(page_title="Portfolio Website",page_icon="😊")

prompt=st.text_area("Enter your prompt here")

if st.button("Generate"):
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
    msg=[("system","""You are an expert web developer with more than 15 years of experience in creating responsive, modern, and clean front-end websites using HTML, CSS, and JavaScript.
Your task is to generate a complete front-end website code based on the user’s prompt.

and the ouput sholuld only contain code for hmtl css and javascript in the below format without any extra text or explanation.

Follow this exact output format (do not add anything extra):         
--html--
[HTML code here]
--html--

--css--
[CSS code here]
--css--

--js--
[JavaScript code here]
--js--

""")]
    
    msg.append(("user", prompt))
    response = llm.invoke(msg)
    
   
    with open("index.html", "w") as f:
        f.write(response.content.split("--html--")[1])
        
    with open("style.css", "w") as f:
        f.write(response.content.split("--css--")[1])
    
    with open("script.js", "w") as f:
        f.write(response.content.split("--js--")[1])
        
    with zipfile.ZipFile("website.zip", "w") as z:
        z.write("index.html")
        z.write("style.css")
        z.write("script.js")
        
    st.download_button("Download",
                       data=open("website.zip","rb"),
                       file_name="website.zip")
    
    st.write("Website Generated Successfully!")
