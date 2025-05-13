from flask import Flask, render_template, request
import google.generativeai as palm
from google.generativeai import ChatSession
import re
from resume_analysis import analyze_resume
import os
from werkzeug.utils import secure_filename
import fitz  # PyMuPDF
import docx

app = Flask(__name__)

# Google AI Studio API key (replace with your own key)
palm.configure(api_key='AIzaSyA2v6FZWoM4UgNYVzFYjRCqOmph5NxmsQs')

def extract_text_from_pdf(file_path):
    text = ""
    doc = fitz.open(file_path)
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

def extract_text_from_file(file):
    filename = secure_filename(file.filename)
    file_ext = os.path.splitext(filename)[1].lower()
    temp_path = os.path.join("temp", filename)
    os.makedirs("temp", exist_ok=True)
    file.save(temp_path)

    text = ""
    try:
        if file_ext == ".pdf":
            text = extract_text_from_pdf(temp_path)
        elif file_ext in [".doc", ".docx"]:
            text = extract_text_from_docx(temp_path)
        else:
            # Unsupported file type fallback
            text = ""
    except Exception as e:
        print(f"Error extracting text from file: {e}")
        text = ""

    # Clean up temp file
    try:
        os.remove(temp_path)
    except Exception as e:
        print(f"Error removing temp file: {e}")

    return text

def generate_feedback_and_score(resume, job_description):
    # Mock response for testing without AI API call
    mock_feedback = "This is a mock feedback for the resume. The resume is well-structured and contains relevant keywords."
    mock_score = 85
    print("Using mock feedback and score for testing.")
    return mock_feedback, mock_score

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        resume_text = request.form.get('resume', '').strip()
        job_description = request.form.get('job_description', '').strip()

        # Check if a file is uploaded
        if 'resume_file' in request.files:
            file = request.files['resume_file']
            if file and file.filename != '':
                extracted_text = extract_text_from_file(file)
                if extracted_text.strip():
                    resume_text = extracted_text

        # Input validation
        errors = []
        if not resume_text:
            errors.append("Please provide resume text or upload a resume file.")
        if not job_description:
            errors.append("Please provide a job description.")

        if errors:
            return render_template('index.html', errors=errors, resume=resume_text, job_description=job_description)

        try:
            feedback, score = generate_feedback_and_score(resume_text, job_description)
            # Analyze resume and generate plot
            plot_url = analyze_resume(resume_text, job_description)
        except Exception as e:
            errors.append(f"An error occurred during analysis: {str(e)}")
            return render_template('index.html', errors=errors, resume=resume_text, job_description=job_description)

        return render_template('result.html', feedback=feedback, score=score, plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
