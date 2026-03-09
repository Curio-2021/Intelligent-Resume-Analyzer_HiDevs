def generate_report(candidate, score):

    if score >= 80:
        recommendation = "Strong Hire"
    elif score >= 60:
        recommendation = "Consider"
    else:
        recommendation = "Reject"
    
    report = {
        "Candidate": candidate["name"],
        "Email": candidate["email"],
        "Skills": candidate["skills"],
        "Experience": candidate["experience"],
        "Match Score": score,
        "Recommendation": recommendation
    }

    return report