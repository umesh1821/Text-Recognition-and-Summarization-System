from Summary2 import Summary as s
from textExtraction import textExtraction
import streamlit as st
from PyPDF2 import PdfReader
from docx import Document
from PIL import Image
import time

def file_manage():
    st.title("Text Recognition and Summarization System")

    sheader = st.sidebar.header("Types of Files",divider="rainbow")

    spdf = st.sidebar.button("Pdf File Summerizer")

    sdocx = st.sidebar.button("Docx File Summerizer")

    stext = st.sidebar.button("Text File Summerizer")

    simage = st.sidebar.button("Image Text Extraction")


    file = st.file_uploader("Please select a file", type=["pdf", "docx", "txt","jpg", "png"])

    text=""

    if file is not None and spdf:
        if file.type == "application/pdf":
            pdf_reader = PdfReader(file)
            for page in pdf_reader.pages:
                text+=page.extract_text()
            st.write(s.mini(text))

    if file is not None and sdocx:
        if file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            doc = Document(file)
            text = " ".join([para.text for para in doc.paragraphs])
            st.write(s.mini(text))

    if file is not None and stext:
        if file.type == "text/plain":
            text = file.getvalue().decode()
            st.write(s.mini(text))

    if file is not None and simage:
        if file.type == "image/jpeg" or file.type == "image/png":
            image = Image.open(file)
            extract = textExtraction.image(image)
            st.write(extract[:-1])

file_manage()
