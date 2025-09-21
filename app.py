from flask import Flask, render_template, request
import PyPDF2
import docx
import re

app = Flask(__name__)

# Store candidates in memory
candidates = []

# Smarter skill patterns
skills_patterns = {
    "Python": r"\bpython\b",
    "Java": r"\bjava\b",
    "SQL": r"\bsql\b",
    "Flask": r"\bflask\b",
    "Machine Learning": r"(machine learning|ml\b)",
    "HTML": r"\bhtml\b",
    "CSS": r"\bcss\b",
    "JavaScript": r"\bjavascript\b"
}

# Extract text from PDF
def read_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + " "
    return text

# Extract text from DOCX
def read_docx(file):
    doc = docx.Document(file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + " "
    return text

# Smarter skill extraction
def extract_skills(text):
    found = []
    text_lower = text.lower()
    for skill, pattern in skills_patterns.items():
        if re.search(pattern, text_lower):
            found.append(skill)
    return found

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        file = request.files.get("resume_file")

        if name and file:
            filename = file.filename.lower()
            if filename.endswith(".pdf"):
                resume_text = read_pdf(file)
            elif filename.endswith(".docx"):
                resume_text = read_docx(file)
            else:
                resume_text = ""

            # Extract skills
            found_skills = extract_skills(resume_text)
            match_score = int(len(found_skills) / len(skills_patterns) * 100)

            # Add candidate to list
            candidates.append((name, ", ".join(found_skills), f"{match_score}%"))

    return render_template("index.html", candidates=candidates)

if __name__ == "__main__":
    app.run(debug=True)
