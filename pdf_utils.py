# pdf_utils.py
import pdfkit

def generate_pdf(html_content, filename):
    pdfkit.from_string(html_content, filename)
