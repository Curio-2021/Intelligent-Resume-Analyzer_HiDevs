import json

def save_report(report, filename="report.json"):
    try:
        with open(filename, "w") as f:
            json.dump(report, f, indent=4)
    except IOError:
        print("Error saving report")

def load_report(filename="report.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None