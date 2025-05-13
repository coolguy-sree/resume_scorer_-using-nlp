import matplotlib.pyplot as plt
import io
import base64
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def analyze_resume(resume, job_description):
    # Extract keywords from job description using TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english', max_features=10)
    tfidf_matrix = vectorizer.fit_transform([job_description])
    keywords = vectorizer.get_feature_names_out()

    # Count occurrences of keywords in resume and job description
    resume_keywords = {kw: resume.lower().count(kw.lower()) for kw in keywords}
    job_keywords = {kw: job_description.lower().count(kw.lower()) for kw in keywords}

    # Create a plot
    fig, ax = plt.subplots()
    index = np.arange(len(keywords))
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, resume_keywords.values(), bar_width,
                     alpha=opacity, color='b', label='Resume')

    rects2 = plt.bar(index + bar_width, job_keywords.values(), bar_width,
                     alpha=opacity, color='g', label='Job Description')

    plt.xlabel('Keywords')
    plt.ylabel('Count')
    plt.title('Keyword Analysis')
    plt.xticks(index + bar_width / 2, keywords, rotation=45, ha='right')
    plt.legend()

    plt.tight_layout()

    # Save plot to a string in base64 format
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    plt.close(fig)
    return 'data:image/png;base64,{}'.format(plot_url)
