# AI-Powered Portfolio Website Generator

This project leverages **Generative AI** to automatically generate a fully functional, responsive **portfolio website**. Using **LangChain** and **Google's Generative AI**, the tool creates **HTML**, **CSS**, and **JavaScript** code based on a simple user prompt.

## Features
- **Resume Parsing**:  Supports both PDF (PyPDF2) and DOCX (python-docx) resume uploads.
- **AI-powered Code Generation**:Automatically generates complete HTML, CSS, and JavaScript based on extracted resume details.
- **Streamlit Interface**: Easy-to-use interface for anyone, regardless of technical background.
- **Downloadable ZIP:**: Get the complete website (index.html, style.css, script.js) in a ZIP file for quick deployment.

## How It Works
![Workflow Diagram Placeholder - A diagram showing flow from Resume Upload -> Text Extraction -> LLM 1 Data Extraction -> LLM 2 Code Generation -> ZIP Download -> Deployment]
1. **Upload Your Resume**: The user uploads a PDF or DOCX file via the Streamlit interface
2. **Text Extraction**: A Language Model processes the text to structure key details (skills, experience, education) and generate the website code. 
3. **Download & Deploy**: your portfolio website.

## Technologies Used
- **Streamlit**: For building the front-end user interface.
- **LangChain**: To interface with **Google's Generative AI** and generate the web code.
- **Google Generative AI**: For natural language processing and code generation.
- **zipfile**: The code is packaged into a ZIP file for the user to download and deploy.
- **PyPDF2 & python-docx**: For document parsing.

## Getting Started

### Prerequisites
1. **Python 3.x** (version 3.7 or above).
2. Install the required dependencies:
   ```bash
   pip install streamlit langchain langchain-google-genai python-dotenv PyPDF2 python-docx

3. Set up your Google API key by adding it to a .env file.

## Running the App:

1. Clone this repository:
   ```bash
    https://github.com/ShubhamMohanty680/AI_Portfolio_Website.git
    cd AI_Portfolio_Website

2. Run the Streamlit app:
   ```bash
   streamlit run main.py
 

