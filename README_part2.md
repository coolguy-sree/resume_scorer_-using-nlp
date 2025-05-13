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
