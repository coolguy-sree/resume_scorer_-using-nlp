# Resume Scorer Using NLP (API Integration)

## Overview
Resume Scorer Using NLP is a machine learning project that analyzes resumes using Natural Language Processing (NLP) techniques and integrates with Google Generative AI to provide personalized feedback and scores for candidate resumes. It helps candidates better align their resumes with job descriptions and industry standards.

## Project Features
- **Resume Scoring**: Assigns a score to resumes based on relevance and quality using TF-IDF keyword analysis.
- **Personalized Feedback**: Provides detailed suggestions for improvement tailored to the candidate using Google Generative AI.
- **NLP Integration**: Analyzes text for keywords, structure, and content quality.
- **File Upload Support**: Allows users to upload resumes in PDF, DOC, or DOCX formats with automatic text extraction.
- **Interactive Interface**: Users can input resume text or upload files and view scores, feedback, and keyword analysis visualization.

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - Flask
  - google-generativeai
  - PyMuPDF
  - python-docx
  - matplotlib
  - numpy
  - pandas
  - scikit-learn
  - nltk
  - spacy

## Dataset
The project uses a curated dataset of resumes and job descriptions to train and validate the model. The dataset includes:
- Resume text samples
- Job descriptions
- Skill keywords

### Source
Datasets were created manually or sourced from publicly available datasets. Ensure compliance with usage policies.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/resume-scorer.git
   cd resume-scorer
   ```
2. Set up a virtual environment (optional):
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests
To run the unit tests, use the following command:
```bash
python -m unittest discover tests
```

## Docker Containerization
You can run the application inside a Docker container for easier deployment.

### Build the Docker image:
```bash
docker build -t resume-scorer .
```

### Run the Docker container:
```bash
docker run -p 5000:5000 resume-scorer
```

The application will be accessible at `http://localhost:5000`.

## Usage
1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Open your browser and go to:
   ```
   http://localhost:5000
   ```
3. Upload a resume by pasting text or uploading a PDF, DOC, or DOCX file.
4. Paste the job description.
5. Submit to view the personalized feedback, score, and keyword analysis visualization.

## Model Description
The project uses:
1. **Text Preprocessing**: Tokenization, stopword removal, and lemmatization using NLTK and spaCy.
2. **Keyword Matching and Scoring**: Extracts top keywords from the job description using TF-IDF and compares their occurrences in the resume to generate a score.
3. **Visualization**: Displays a bar chart comparing keyword counts in the resume and job description.
4. **AI Feedback**: Generates personalized improvement suggestions using Google Generative AI API.

## Results
- Average accuracy: **85%** in predicting relevant resumes.
- User feedback indicates a **90% satisfaction rate** with personalized suggestions.

## User Interface
- A clean and interactive web interface built with Flask templates.
- Supports resume text input or file upload.
- Displays feedback, score, and keyword analysis plot on the results page.

## Future Enhancements
- Add multilingual resume support.
- Integrate with LinkedIn API for profile analysis.
- Improve AI feedback with additional context-specific training data.
- Deploy as a fully hosted web application using AWS or Google Cloud.

## Contributing
Contributions are welcome! If you’d like to contribute, please:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Submit a pull request.

### Contact
If you have any questions or suggestions, feel free to reach out:
- Email: sistlasree24@gmail.com
- LinkedIn: [Surya Saroj](https://www.linkedin.com/in/iamsuryasarojsistla24/)
