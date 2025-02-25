import re
import spacy

# Load NLP model
nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    """Preprocess the extracted resume text by removing unwanted characters."""
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove special characters
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra spaces
    return text

def preprocess_resume(text):
    """Run NLP preprocessing: Tokenization, Lemmatization, and Stopword Removal."""
    doc = nlp(text)
    processed_text = ' '.join([token.lemma_ for token in doc if not token.is_stop])
    return processed_text
