import unittest
from resume_analysis import analyze_resume

class TestResumeAnalysis(unittest.TestCase):

    def test_analyze_resume_basic(self):
        resume = "Python Flask AI AI AI NLP"
        job_description = "Python AI AI AI AI Flask Flask NLP"
        plot_url = analyze_resume(resume, job_description)
        self.assertTrue(plot_url.startswith('data:image/png;base64,'))

if __name__ == '__main__':
    unittest.main()
