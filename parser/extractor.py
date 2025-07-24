import spacy
import re

nlp = spacy.load("en_core_web_sm")

SKILLS_DB = ["python", "java", "c++", "machine learning", "deep learning", "excel", "sql", "django", "flask"]

def extract_entities(text):
    doc = nlp(text)
    entities = {"Name": "", "Email": "", "Phone": "", "Skills": [], "Education": "", "Experience": ""}
    
    for ent in doc.ents:
        if ent.label_ == "PERSON" and not entities["Name"]:
            entities["Name"] = ent.text
        if ent.label_ == "ORG" and "university" in ent.text.lower():
            entities["Education"] = ent.text

    email_match = re.findall(r'\S+@\S+', text)
    phone_match = re.findall(r'\+?\d[\d\- ]{8,}\d', text)

    if email_match:
        entities["Email"] = email_match[0]
    if phone_match:
        entities["Phone"] = phone_match[0]

    entities["Skills"] = [skill for skill in SKILLS_DB if skill.lower() in text.lower()]

    exp_match = re.search(r'(?i)(experience|work experience)(.*?)(education|skills)', text, re.S)
    if exp_match:
        entities["Experience"] = exp_match.group(2).strip()

    return entities
