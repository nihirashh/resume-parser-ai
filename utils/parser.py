import PyPDF2
import re

# Extract text from PDF
def extract_text(file_path):
    text = ""

    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        
        for page in reader.pages:
            text += page.extract_text()

    return text


# Extract email
def extract_email(text):
    email = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", text)
    return email[0] if email else "Not found"


# Extract name (first non-empty line)
def extract_name(text):
    lines = text.split("\n")
    
    for line in lines:
        if line.strip():
            return line.strip()
    
    return "Not found"


# Extract phone number
def extract_phone(text):
    phone = re.findall(r'\+?\d[\d\s\-]{8,}\d', text)
    return phone[0] if phone else "Not found"


# Extract skills
def extract_skills(text):
    skills_list = ["python", "c", "java", "html", "css", "javascript", "sql"]
    
    found_skills = []
    text = text.lower()

    for skill in skills_list:
        if skill in text:
            found_skills.append(skill)

    return found_skills


# Extract education (basic keyword matching)
def extract_education(text):
    education_keywords = [
        "b.tech", "bachelor", "master", "m.tech", "b.sc", "m.sc",
        "engineering", "university", "college", "school"
    ]

    lines = text.lower().split("\n")
    found = []

    for line in lines:
        for word in education_keywords:
            if word in line:
                found.append(line.strip())
                break

    return found if found else ["Not found"]