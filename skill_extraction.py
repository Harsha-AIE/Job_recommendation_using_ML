import spacy

# Load SpaCy model after installation
nlp = spacy.load('en_core_web_sm')

def extract_skills(text):
    doc = nlp(text)
    # You may need to customize the extraction rule based on your dataset and label
    skills = [ent.text for ent in doc.ents if ent.label_ == 'SKILL']  # Adjust label based on custom NER
    return skills
