import re

def run_static_checks(code: str):
    issues = []

    if "print(" in code:
        issues.append("Avoid using print statements in production code.")

    functions = re.findall(r"def .*?:([\s\S]*?)(?=\ndef|\Z)", code)
    for f in functions:
        if len(f.split("\n")) > 50:
            issues.append("Function too long (>50 lines).")

    if re.search(r"\b\d{2,}\b", code):
        issues.append("Magic numbers detected.")

    return issues
