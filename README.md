ATS Resume Analyzer


The ATS Resume Analyzer evaluates the compatibility of a resume with a job description. It uses a generative AI model to calculate a match percentage, identify missing keywords, and generate a profile summary to help optimize resumes for Applicant Tracking Systems (ATS).

How It Works:
Upload Resume: Users upload a PDF of their resume.
Enter Job Description: Paste the job description for the position you're interested in.
Receive Results:
JD Match: A percentage that shows how closely your resume matches the job description.
Missing Keywords: A list of important keywords that are missing in your resume, which could improve its ATS compatibility.
Profile Summary: Suggestions on how to improve the resume to increase chances of getting noticed by ATS.

Code:
ATS_Resume_Analyzer/
│
├── app.py             # Main application file (Streamlit app)
├── .env               # Stores sensitive information like API keys (DO NOT commit to public repos)
├── requirements.txt   # List of dependencies for the project
├── README.md          # Project documentation
├── LICENSE            # License for the project
└── assets/            # Folder for assets like images or additional files

Blame:
During development, one of the key challenges was ensuring the resume extraction from PDFs was accurate. PyPDF2 was chosen for its simplicity and compatibility, but there were instances where certain PDFs didn't extract text cleanly. We overcame this by ensuring the resumes are formatted correctly before processing.

