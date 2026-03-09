# Intelligent Resume Analyzer

A Python application that automates resume screening by parsing resumes, matching candidates to job requirements, and generating hiring recommendations.
This project is automatically generated.

## Installation

```sh
pip install -r requirements.txt
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
│
├── main.py # Runs the application
├── parser.py # Resume parsing logic
├── matcher.py # Candidate-job matching algorithm
├── report.py # Report generation
├── storage.py # JSON file operations
├── resume.txt # Example resume
├── requirements.txt
gitignore
README.md

## Requirements

- Python 3.8+
- No external libraries required (uses Python standard library)