from skill_extractor import extract_skills


def compare_skills(resume_skills, job_description):

    if not job_description:
        return [], [], 0

    job_skills = extract_skills(job_description)

    resume_skills_lower = set(skill.lower() for skill in resume_skills)

    missing_skills = []
    matched_skills = []

    for skill in job_skills:
        if skill.lower() in resume_skills_lower:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    if len(job_skills) == 0:
        score = 0
    else:
        score = int((len(matched_skills) / len(job_skills)) * 100)

    return job_skills, missing_skills, score
