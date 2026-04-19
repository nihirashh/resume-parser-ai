# Resume Parser AI
A simple AI-based web application that extracts key information from resumes.

# Live Demo
(https://resume-parser-ai-5url.onrender.com/)

# Features
* Upload Resume (PDF)
* Extract Name, Email, Phone
* Identify Skills
* Extract Education details
* Clean and modern UI

# Tech Stack
* Python (Flask)
* HTML, CSS
* PyPDF2
* Regex & Keyword Matching

# Project Structure
resume-parser-ai/
│── app.py
│── requirements.txt
│── templates/
│   ├── index.html
│   └── result.html
│── static/
│   └── static.css
│── uploads/
│── utils/
│   └── parser.py

# How to Run Locally
1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Run the app:
   python app.py
4. Open:
   http://127.0.0.1:5000/

# Limitations
* Rule-based extraction (may not work for all formats)
* Basic keyword matching for education

# Future Improvements
* Use NLP (spaCy) for better accuracy
* Add experience extraction
* Improve UI further

---
👩‍💻 Built as part of an AI Internship.
