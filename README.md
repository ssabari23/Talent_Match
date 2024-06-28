# Talent Match App README

## Overview
The Talent Match App is a Streamlit application that helps HR teams evaluate resumes against job descriptions using machine learning. It leverages Google's Gemini Pro API to generate content and score resumes based on job descriptions, making it easier to identify the best candidates for a job.

## Installation
### Prerequisites
- Python 3.7 or higher
- Streamlit
- google-generativeai
- PyPDF2
- python-dotenv
- pandas
- spire.doc

## Running the App
To run the Streamlit application, use the following command:
```bash
streamlit run app.py

## Application Features
Upload Job Description
Users can upload job descriptions in .txt, .pdf, or .docx formats.
The application will extract and display the job description text.
Upload Resumes
Users can upload multiple resumes in .pdf or .docx formats.
The application extracts text from the resumes for further processing.
Evaluate Resumes
The application uses Google's Gemini Pro API to evaluate resumes based on the provided job description.
The results are displayed in a table, showing the candidate's name, matching score, strengths, and weaknesses.
Interactive Features
Users can set a score threshold to filter resumes.
View detailed resume content by clicking "View Resume".
Select resumes to download their details as an Excel file.
Navigate back to the home page to start a new evaluation.
Upload Job Description
Upload Job Description:
Users can upload job descriptions in .txt, .pdf, or .docx formats.
The application will extract and display the job description text.
Upload Resumes
Upload Resumes:
Users can upload multiple resumes in .pdf or .docx formats.
The application extracts text from the resumes for further processing.
Evaluate Resumes
Evaluate Resumes:
The application uses Google's Gemini Pro API to evaluate resumes based on the provided job description.
The results are displayed in a table, showing the candidate's name, matching score, strengths, and weaknesses.
Interactive Features
Interactive Features:
Users can set a score threshold to filter resumes.
View detailed resume content by clicking "View Resume".
Select resumes to download their details as an Excel file.
Navigate back to the home page to start a new evaluation.
Code Structure
app.py
This is the main application file containing the following sections:

Imports:

Essential libraries and modules are imported, including Streamlit, google-generativeai, PyPDF2, dotenv, pandas, and spire.doc.
Environment Variable Loading:

Loads environment variables using dotenv.
Function Definitions:

read_docx(file): Reads text from a .docx file.
get_gemini_response(input): Gets a response from the Gemini Pro API.
input_pdf_text(uploaded_file): Extracts text from a .pdf file.
display_results(results): Displays the results table with interactive features.
Streamlit App Logic:

Initializes session state for storing results, job descriptions, and resume texts.
Handles file uploads for job descriptions and resumes.
Submits the job description and resumes for evaluation using the Gemini Pro API.
Displays results and provides options to filter, view, select, and download resume details.
Configuration
Ensure you have set up the Google API key correctly in your .env file. The API key is used to authenticate and make requests to the Gemini Pro API.

Troubleshooting
If the app fails to start, ensure all required packages are installed.
Verify the Google API key is correctly set in the .env file.
Check for any file permission issues when uploading files.
Future Enhancements
Add support for additional file formats for resumes and job descriptions.
Improve the UI/UX for better user interaction.
Implement more robust error handling and logging.
