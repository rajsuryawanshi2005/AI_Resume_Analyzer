from flask import Flask, render_template, request
import os

from resume_parser import extract_text
from skill_extractor import extract_skills
from matcher import compare_skills

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def generate_suggestions(missing_skills):
    suggestions = []

    for skill in missing_skills:
        suggestions.append(f"Consider adding projects or experience related to {skill}")

    if not suggestions:
        suggestions.append("Great! Your resume matches most of the job requirements.")

    return suggestions


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        file = request.files["resume"]
        job_desc = request.form["jobdesc"]

        if file.filename == "":
            return "No file selected"

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        text = extract_text(filepath)

        skills = extract_skills(text)

        job_skills, missing_skills, score = compare_skills(skills, job_desc)

        suggestions = generate_suggestions(missing_skills)

        return render_template(
            "result.html",
            skills=skills,
            job_skills=job_skills,
            missing=missing_skills,
            score=score,
            suggestions=suggestions
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
