# Talent Match App 

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
```
## Application Features
### Upload Job Description
Users can upload job descriptions in  .docx formats.
The application will extract and display the job description text.
### Upload Resumes
Users can upload multiple resumes in .pdf formats.
The application extracts text from the resumes for further processing.
### Evaluate Resumes
The application uses Google's Gemini Pro API to evaluate resumes based on the provided job description.
The results are displayed in a table, showing the candidate's name, matching score and options to view respective resumes and also select the candidate.
### Interactive Features
Users can set a score threshold to filter resumes.
View detailed resume content by clicking "View Resume".
Select resumes to download their details as an Excel file.
Navigate back to the home page to start a new evaluation.

### Troubleshooting
If the app fails to start, ensure all required packages are installed.
Verify the Google API key is correctly set in the .env file.
Check for any file permission issues when uploading files.

### Future Enhancements
Add support for additional file formats for resumes and job descriptions.
Improve the UI/UX for better user interaction.
Implement more robust error handling and logging.

### Some Useful Links
https://sanjayc.medium.com/compute-the-match-percentage-of-a-candidate-for-a-job-role-aa3adc7bfbb5
https://noerbarry.medium.com/linkedin-resume-validation-using-ats-system-method-with-nlp-in-python-streamlit-4d0be4da4e6
https://github.com/krishnaik06/Google-Gemini-Crash-Course/tree/main/atsllm
https://github.com/scsanjay/jd_resume_match_percentage



