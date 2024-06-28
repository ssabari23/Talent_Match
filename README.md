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

### Step-by-Step Guide
1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-repository/talent-match-app.git
    cd talent-match-app
    ```

2. **Install the required packages:**
    ```bash
    pip install streamlit google-generativeai PyPDF2 python-dotenv pandas spire.doc
    ```

3. **Set up the environment variables:**
    - Create a `.env` file in the root directory.
    - Add your Google API key to the `.env` file:
      ```
      GOOGLE_API_KEY=your_google_api_key_here
      ```

## Running the App
To run the Streamlit application, use the following command:
```bash
streamlit run app.py
