import re

SKILLS_LIST = [
    "python","java","javascript","c++","c#","html","css","react","angular",
    "vue","node.js","django","flask","sql","mysql","mongodb","git",
    "aws","docker","kubernetes","machine learning","deep learning",
    "data science","tensorflow","pytorch","pandas","numpy","excel",
    "linux","rest api","graphql","microservices"
]


def extract_skills(text):

    if not text:
        return []

    text_lower = text.lower()
    found_skills = set()

    for skill in SKILLS_LIST:
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'

        if re.search(pattern, text_lower):
            found_skills.add(skill)

    return list(found_skills)
