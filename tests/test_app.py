import unittest
from unittest.mock import patch, MagicMock
import io
import os
from app import extract_text_from_pdf, extract_text_from_docx, extract_text_from_file, generate_feedback_and_score
import tempfile

class TestAppFunctions(unittest.TestCase):

    def test_extract_text_from_pdf(self):
        # Create a temporary PDF file for testing
        # Since creating a real PDF is complex, we will mock fitz.open
        with patch('app.fitz.open') as mock_fitz_open:
            mock_doc = MagicMock()
            mock_page = MagicMock()
            mock_page.get_text.return_value = "Sample PDF text"
            mock_doc.__iter__.return_value = [mock_page]
            mock_fitz_open.return_value = mock_doc

            text = extract_text_from_pdf("dummy.pdf")
            self.assertEqual(text, "Sample PDF text")

    def test_extract_text_from_docx(self):
        # Mock docx.Document to return paragraphs
        with patch('app.docx.Document') as mock_docx_doc:
            mock_doc = MagicMock()
            mock_para1 = MagicMock()
            mock_para1.text = "Paragraph 1"
            mock_para2 = MagicMock()
            mock_para2.text = "Paragraph 2"
            mock_doc.paragraphs = [mock_para1, mock_para2]
            mock_docx_doc.return_value = mock_doc

            text = extract_text_from_docx("dummy.docx")
            self.assertEqual(text, "Paragraph 1\nParagraph 2")

    def test_extract_text_from_file_pdf(self):
        # Mock file object with filename and save method
        mock_file = MagicMock()
        mock_file.filename = "test.pdf"
        def save(path):
            with open(path, 'w') as f:
                f.write("dummy")
        mock_file.save.side_effect = save

        with patch('app.extract_text_from_pdf', return_value="Extracted PDF text") as mock_pdf:
            text = extract_text_from_file(mock_file)
            self.assertEqual(text, "Extracted PDF text")

    def test_extract_text_from_file_docx(self):
        mock_file = MagicMock()
        mock_file.filename = "test.docx"
        def save(path):
            with open(path, 'w') as f:
                f.write("dummy")
        mock_file.save.side_effect = save

        with patch('app.extract_text_from_docx', return_value="Extracted DOCX text") as mock_docx:
            text = extract_text_from_file(mock_file)
            self.assertEqual(text, "Extracted DOCX text")

    @patch('app.palm.chat')
    def test_generate_feedback_and_score(self, mock_chat):
        mock_response = MagicMock()
        mock_response.last = "Great resume! **Overall Score:** 85"
        mock_chat.return_value = mock_response

        feedback, score = generate_feedback_and_score("resume text", "job description")
        self.assertIn("Great resume!", feedback)
        self.assertEqual(score, 85)

if __name__ == '__main__':
    unittest.main()
