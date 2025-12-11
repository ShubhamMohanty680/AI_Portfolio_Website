# Portfolio Website Generator with AI

This project leverages **Generative AI** to automatically generate a fully functional, responsive **portfolio website**. Using **LangChain** and **Google's Generative AI**, the tool creates **HTML**, **CSS**, and **JavaScript** code based on a simple user prompt.

## Features
- **AI-powered website generation**: Automatically generates HTML, CSS, and JavaScript based on your input.
- **Streamlit Interface**: Easy-to-use interface for anyone, regardless of technical background.
- **Downloadable ZIP**: Get the complete website (index.html, style.css, script.js) in a ZIP file for quick deployment.
- **Customizable**: Edit the generated code to personalize the website further.

## How It Works
1. **Enter a description** of the website you want in the text area.
2. The AI generates the **HTML**, **CSS**, and **JavaScript** code.
3. The code is saved and packaged into a **ZIP file** containing the necessary website files.
4. Download the ZIP file and **deploy** your portfolio website.

## Technologies Used
- **Streamlit**: For building the front-end user interface.
- **LangChain**: To interface with **Google's Generative AI** and generate the web code.
- **Google Generative AI**: For natural language processing and code generation.
- **zipfile**: To bundle the generated files into a downloadable ZIP.

## Getting Started

### Prerequisites
1. **Python 3.x** (version 3.7 or above).
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   
3. Set up your Google API key by adding it to a .env file.

## Running the App:

1. Clone this repository:
   
    git clone https://github.com/your-username/portfolio-website-generator.git
    cd portfolio-website-generator

2. Run the Streamlit app:

   streamlit run app.py
 

