from flask import Flask, render_template, request
import os
from utils.parser import (
    extract_text,
    extract_skills,
    extract_email,
    extract_name,
    extract_phone,
    extract_education
)

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        file = request.files["resume"]

        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            text = extract_text(filepath)

            name = extract_name(text)
            email = extract_email(text)
            phone = extract_phone(text)
            skills = extract_skills(text)
            education = extract_education(text)

            return render_template(
                "result.html",
                name=name,
                email=email,
                phone=phone,
                skills=skills,
                education=education
            )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)