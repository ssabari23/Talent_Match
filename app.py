import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json
import pandas as pd
import tempfile
from spire.doc import Document
from io import BytesIO

load_dotenv()  ## load all our environment variables
GOOGLE_API_KEY = "insert api key here"
genai.configure(api_key=GOOGLE_API_KEY)

# Function to read docx file JD
def read_docx(file):
    # Create a Document object
    document = Document()
    # Load a Word document
    document.LoadFromFile(file)
    # Extract the text of the document
    document_text = document.GetText()
    return document_text


def get_gemini_response(input):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(input)
    return response.text


def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text


# Prompt Template
input_prompt = """
Hey Act Like a skilled or very experienced ATS (Application Tracking System)
with a deep understanding of Data Science and Machine Learning. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive. Assign the percentage Matching based 
on JD. Also extract the candidate full name and his strengths and weaknesses comparing it with job requirement.

**Resumes:**

{resumes}

**Job Description:**

{jd}

I want the response in a list of JSON strings having the structure:
[
    {{"Name":"","JD Match":"%","MissingKeywords":[],"Profile Summary":"","Strengths":"","Weakness":""}},
    
]
"""

## Streamlit app
st.title("Talent Match")


# State management
if "results" not in st.session_state:
    st.session_state.results = None
    st.session_state.job_description = None
    st.session_state.resume_texts = []

# Function to display the result table
def display_results(results):
    st.header("Resume Scores")
    threshold = st.slider("Score Threshold", 0, 100, 0)
    data = []
    selected_rows = []
    for i, item in enumerate(results):
        if int(item["JD Match"].replace("%", "")) >= threshold:
            data.append([item["Name"], item["JD Match"], f"View Resume {i+1}", f"select_{i+1}"])

    df = pd.DataFrame(data, columns=["Name", "Score", "Action", "Select"])
    col1, col2, col3, col4 = st.columns(4)
    col1.write("Name")
    col2.write("Score")
    col3.write("Resume")
    col4.write("Select")    

    for index, row in df.iterrows():
        col1, col2, col3, col4 = st.columns(4)
        col1.write(row["Name"])
        col2.write(row["Score"])
        if col3.button("View Resume", key=f"view_{index}"):
            st.write(f"Resume {index+1} content")
            st.text(st.session_state.resume_texts[index])
        if col4.checkbox("Select", key=row["Select"]):
            selected_rows.append(index)

    if st.button("Download Selected as Excel"):
        selected_data = df.iloc[selected_rows][["Name", "Score"]]
        buffer = BytesIO()
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            selected_data.to_excel(writer, index=False)
        st.download_button(
            label="Download Excel file",
            data=buffer,
            file_name="selected_resumes.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    if st.button("Go to Home Page"):
        st.session_state.results = None
        st.session_state.job_description = None
        st.session_state.resume_texts = []

# Page logic
if st.session_state.results is None:
    st.header("Upload Job Description")
    job_description_file = st.file_uploader("Choose a job description file", type=["txt", "pdf", "docx"])

    if job_description_file is not None:
        # Save the uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as temp_file:
            temp_file.write(job_description_file.getbuffer())
            temp_file_path = temp_file.name

        job_description = read_docx(temp_file_path)
        st.text_area("Job Description", job_description, height=300)
        os.remove(temp_file_path)  # Clean up the temporary file
        st.session_state.job_description = job_description

    # Resume Upload
    st.header("Upload Resumes")
    uploaded_files = st.file_uploader("Choose resume files", type=["pdf", "docx"], accept_multiple_files=True)
    submit = st.button("Submit")

    if submit and uploaded_files is not None:
        resume_texts = []
        for uploaded_file in uploaded_files:
            resume_texts.append(input_pdf_text(uploaded_file))
        
        resumes_string = "\n".join(f"resume:{text}" for text in resume_texts)
        prompt = input_prompt.format(resumes=resumes_string, jd=st.session_state.job_description)
        response = get_gemini_response(prompt)

        # Parse the JSON list response
        try:
            response_list = json.loads(response)
            st.session_state.results = response_list
            st.session_state.resume_texts = resume_texts
        except json.JSONDecodeError:
            st.error("Error: Invalid response format")
else:
    display_results(st.session_state.results)
