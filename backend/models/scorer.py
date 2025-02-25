import spacy

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Define important resume sections
REQUIRED_SECTIONS = ["education", "skills", "experience", "projects", "certifications"]

def analyze_resume(text):
    """Analyze the resume text and return a score & suggestions."""
    doc = nlp(text)
    entities = {ent.label_.lower(): ent.text for ent in doc.ents}
    
    # Improved scoring logic
    section_coverage = sum(1 for section in REQUIRED_SECTIONS if section in entities)
    score = (section_coverage / len(REQUIRED_SECTIONS)) * 100
    score = round(score, 2)
    
    suggestions = []
    for section in REQUIRED_SECTIONS:
        if section not in entities:
            suggestions.append(f"Consider adding a {section.capitalize()} section to your resume.")
    
    return {"score": score, "suggestions": suggestions}
