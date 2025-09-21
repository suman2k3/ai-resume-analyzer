AI-Powered Resume Analyzer

A web application that automatically analyzes resumes, extracts skills, and ranks candidates based on their skill match. Built with Flask, Python, and regex-based skill extraction.

Live demo: https://ai-resume-analyzer-1-ie6h.onrender.com/

Features

Upload PDF or DOCX resumes

Extracts key skills like Python, Java, SQL, Flask, HTML, CSS, JavaScript, and Machine Learning

Calculates a match percentage based on skills found

Displays a dynamic candidate ranking table

Tech Stack

Backend: Python, Flask

Frontend: HTML, JavaScript (no templates used, fully static HTML)

Libraries: PyPDF2, python-docx, regex

Installation (Local)

Clone the repository:

git clone https://github.com/suman2k3/ai-resume-analyzer.git
cd ai-resume-analyzer


Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt


Run the app:

python app.py


Open http://127.0.0.1:5000
 in your browser.

Usage

Enter candidate name

Upload a PDF or DOCX resume

Submit the form

View the Candidate Rankings table with skills and match percentage

Project Structure
ai-resume-analyzer/
├─ app.py              # Flask backend
├─ index.html          # Frontend HTML page
├─ requirements.txt
└─ README.md

Notes

Currently, candidates are stored in memory. Restarting the server will reset the data.

Regex-based skill extraction is used; no heavy NLP library is required.
