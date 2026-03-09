from parser import parse_resume
from matcher import calculate_match
from report import generate_report
from storage import save_report

skill_list = ["python", "java", "sql", "machine learning", "data analysis"]

job_requirements = {
    "skills": ["python", "sql", "machine learning"],
    "experience": 3
}

def main():
    with open("resume.txt", "r") as f:
        resume_text = f.read()
    candidate = parse_resume(resume_text, skill_list)
    score = calculate_match(candidate, job_requirements)
    report = generate_report(candidate, score)
    save_report(report)
    print("\nResume Analysis Report\n")
    for key, value in report.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()