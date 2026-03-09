def calculate_match(candidate, job_requirements):
    required_skills = job_requirements["skills"]
    experience_needed = job_requirements["experience"]

    skill_matches = len(set(candidate["skills"]) & set(required_skills))
    skill_score = (skill_matches / len(required_skills)) * 70

    exp_score = min(candidate["experience"] / experience_needed, 1) * 30

    total_score = skill_score + exp_score

    return round(total_score, 2)