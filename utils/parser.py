import PyPDF2

def extract_text(file_path):
    text = ""

    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        
        for page in reader.pages:
            text += page.extract_text()

    return text

def extract_skills(text):
    skills_list = ["python", "c", "java", "html", "css", "javascript", "sql"]

    found_skills = []

    text = text.lower()

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills

import re

def extract_email(text):
    email = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", text)
    return email[0] if email else "Not found"

def extract_name(text):
    lines = text.split("\n")
    
    for line in lines:
        if line.strip():
            return line.strip()
    
    return "Not found"