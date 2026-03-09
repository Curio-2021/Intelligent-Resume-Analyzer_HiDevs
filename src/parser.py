import re

def extract_email(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+"
    match = re.search(pattern, text)
    return match.group(0) if match else None

def extract_name(text):
    lines = text.split("\n")
    return lines[0].strip()

def extract_skills(text, skill_list):
    text=text.lower()
    found_skills=[]

    for skill in skill_list:
        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills

def extract_experience(text):
    pattern = r"(\d+)\s+years"
    match = re.search(pattern, text.lower())
    return int(match.group(1)) if match else 0

def parse_resume(text, skill_list):
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "skills": extract_skills(text, skill_list),
        "experience": extract_experience(text)
    }