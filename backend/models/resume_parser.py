import fitz  # PyMuPDF
from backend.utils.preprocessing import clean_text, preprocess_resume

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file and preprocess it."""
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text("text") + "\n"
    except Exception as e:
        print(f"Error extracting text: {e}")
    
    # Clean and preprocess the extracted text
    text = clean_text(text)
    text = preprocess_resume(text)
    
    return text.strip()
