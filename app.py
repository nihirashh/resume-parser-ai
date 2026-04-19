from flask import Flask, render_template, request
import os
from utils.parser import extract_text, extract_skills, extract_email, extract_name

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

            # Extract data
            text = extract_text(filepath)
            skills = extract_skills(text)
            email = extract_email(text)
            name = extract_name(text)

            return render_template(
                "result.html",
                name=name,
                email=email,
                skills=skills
            )

    return render_template("index.html")


if __name__ == "__main__":
    app.run()