import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv()  # Load environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Gemini Pro Response
def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

# Extract and concatenate text from all pages of the given PDF file
def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

# Prompt Template --> The better the prompt, the better the result
input_prompt = """
Hey, act like a skilled or very experienced ATS (Applicant Tracking System) with a deep understanding of the tech field, software engineering, data science, data analysis, and big data engineering. Your task is to evaluate the resume based on the given job description.
You must consider that the job market is very competitive and provide the best assistance for improving resumes. Assign the percentage match based on the job description and list the missing keywords with high accuracy.  
resume: {text}
description: {jd}

I want the response in one single string having the structure:
{{"JD Match":"%","MissingKeywords":[],"Profile Summary":""}}
"""

# Streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")

# User inputs for job description and resume
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader("Upload Your Resume", type="pdf", help="Please upload the PDF")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        # Extract text from uploaded PDF
        text = input_pdf_text(uploaded_file)
        
        # Get the response from Gemini AI model
        response = get_gemini_response(input_prompt.format(text=text, jd=jd))
        
        try:
            # Parse the JSON response
            response_data = json.loads(response)

            # Extract data from response
            jd_match = response_data.get("JD Match", "N/A")
            missing_keywords = response_data.get("MissingKeywords", [])
            profile_summary = response_data.get("Profile Summary", "N/A")

            # Format the output
            formatted_output = f"""
            **Job Description Match Evaluation:**

            - **JD Match:** {jd_match}%

            - **Missing Keywords:**
              {'\n   - '.join(missing_keywords) if missing_keywords else "No missing keywords found."}

            ---

            **Profile Summary:**
            {profile_summary}
            """

            # Display the formatted output
            st.subheader("Results")
            st.markdown(formatted_output)

            # Show Profile Summary in a multi-line text box without scrolling
            st.text_area("Profile Summary", value=profile_summary, height=250)

        except Exception as e:
            st.error(f"Error processing the response: {e}")
