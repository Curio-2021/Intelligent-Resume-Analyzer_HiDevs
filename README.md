# Intelligent Resume Analyzer

A Python application that automates resume screening by parsing resumes, matching candidates to job requirements, and generating hiring recommendations.
This project is automatically generated.

## Installation

```sh
pip install -r requirements.txt
```

## How to Run

1. Clone the repository
```sh
git clone <repo-url>
cd src
```

2. Run the program
```sh
python main.py
```

## Features

- Extracts candidate information from resumes
  - Name
  - Email
  - Skills
  - Experience
- Calculates match scores (0–100)
- Generates hiring recommendations
- Saves reports in JSON format
- User input for job requirements

## Project Structure
src/
<br>
│
<br>
├── main.py # Runs the application
<br>
├── parser.py # Resume parsing logic
<br>
├── matcher.py # Candidate-job matching algorithm
<br>
├── report.py # Report generation
<br>
├── storage.py # JSON file operations
<br>
├── resume.txt # Example resume
<br>
├── requirements.txt
<br>
gitignore
<br>
README.md

## Requirements

- Python 3.8+
- No external libraries required (uses Python standard library)
