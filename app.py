import streamlit as st
import dotenv
import langchain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import zipfile
import os
from pathlib import Path
import PyPDF2
from io import BytesIO
from docx import Document

# Load environment variables
dotenv.load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("gemini")

# Streamlit page setup
st.title("AI-Generated Portfolio from Resume")
st.set_page_config(page_title="AI Portfolio Generator", page_icon="📜")

# File upload
upload_file = st.file_uploader("Upload your resume (PDF, Word format)", type=["pdf", "docx"])

col1, col2 = st.columns(2)
with col1:
    if st.button("Generate Portfolio"):
        if upload_file is not None:
            file_extension = Path(upload_file.name).suffix.lower()
            content = ""

            # Extract content based on file type
            if file_extension == ".pdf":
                with BytesIO(upload_file.read()) as f:
                    reader = PyPDF2.PdfReader(f)
                    for page in reader.pages:
                        content += page.extract_text()
                st.subheader("Preview of Extracted Resume Content:")
                st.write(content)
                st.success("PDF uploaded successfully!")

            elif file_extension == ".docx":
                doc = Document(upload_file)
                for para in doc.paragraphs:
                    content += para.text + "\n"
                st.subheader("Preview of Extracted Resume Content:")
                st.write(content)
                st.success("DOCX uploaded successfully!")

            else:
                st.warning("Unsupported file format. Please upload a PDF or DOCX file.")

            # Set up AI model for portfolio generation
            llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
            msg = [("system", """You are an expert web developer with more than 15 years of experience in creating responsive, modern, and clean front-end websites using HTML, CSS, and JavaScript. Your task is to generate a complete front-end website code based on the user’s prompt. Your output should only contain code for HTML, CSS, and JavaScript in the following exact format (do not add anything extra): 
--html-- 
[HTML code here] 
--html-- 

--css-- 
[CSS code here] 
--css-- 

--js-- 
[JavaScript code here] 
--js--""")]

            prompt = f"Generate a multi-section personal portfolio website based on the following resume details:\n{content} by extracting key information such as name, contact details, skills, experience, projects, and education."
            msg.append(("user", prompt))
            response = llm.invoke(msg)

            # Check the content type of the response and split accordingly
            if isinstance(response.content, str):
                # html_content = response.content.split("--html--")[1].split("--css--")[0].strip()
                html_content = response.content.split("--html--")[1]
                css_content = response.content.split("--css--")[1]
                js_content = response.content.split("--js--")[1]

                # Write HTML, CSS, and JS to files
                with open("index.html", "w") as f:
                    f.write(html_content)
                with open("style.css", "w") as f:
                    f.write(css_content)
                with open("script.js", "w") as f:
                    f.write(js_content)

                # Zip the files
                with zipfile.ZipFile("website.zip", "w") as z:
                    z.write("index.html")
                    z.write("style.css")
                    z.write("script.js")
                
                st.write("Website Generated Successfully!")

            else:
                st.error("Error: The response content is not in the expected format.")
            
        else:
            st.warning("Please upload a resume file to generate the portfolio.")

with col2:
    if os.path.exists("website.zip"):
        st.download_button("Download Website", data=open("website.zip", "rb"), file_name="website.zip")
       

