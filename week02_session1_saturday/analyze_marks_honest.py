import csv


SUBJECTS = ["math", "science", "english", "history", "art"]


def load_marks(file_path):
    """Load the CSV as a list of dict rows."""
    with open(file_path, "r", newline="") as f:
        return list(csv.DictReader(f))


def get_score(value):
    """Return an integer score, or None if the value cannot be parsed.

    This is the honest version of Shloka's `safe_int`. Returning None
    instead of 0 means aggregation functions can SKIP bad data instead
    of silently corrupting the results.
    """
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def subject_averages(rows):
    """Compute the average per subject, skipping missing/malformed scores."""
    averages = {}
    for subject in SUBJECTS:
        scores = [get_score(row.get(subject, "")) for row in rows]
        valid = [s for s in scores if s is not None]
        if valid:
            averages[subject] = round(sum(valid) / len(valid), 2)
        else:
            averages[subject] = None
    return averages


def total_marks(row):
    """Sum all valid subject scores in a row. Skips invalid cells."""
    return sum(get_score(row.get(s, "")) or 0 for s in SUBJECTS)


def top_student(rows):
    """Return (name, total) for the student with the highest valid total."""
    named = [r for r in rows if r.get("name", "").strip()]
    if not named:
        return None, 0
    best = max(named, key=total_marks)
    return best["name"], total_marks(best)


def report_issues(rows):
    """Report rows and cells that had missing or malformed data."""
    issues = []
    for i, row in enumerate(rows, start=2):  # header is row 1
        if not row.get("name", "").strip():
            issues.append(f"Row {i}: missing student name")
        for subject in SUBJECTS:
            raw = row.get(subject)
            if raw is None:
                issues.append(f"Row {i}: missing '{subject}' column")
            elif raw.strip() == "":
                issues.append(f"Row {i}: blank '{subject}' cell")
            elif get_score(raw) is None:
                issues.append(f"Row {i}: '{subject}' has non-numeric value '{raw}'")
    return issues


def print_summary(rows):
    """Print a summary that reports missing data honestly."""
    print(f"Total students loaded: {len(rows)}")
    print()

    print("Subject averages (based on valid cells only):")
    for subject, avg in subject_averages(rows).items():
        display = avg if avg is not None else "no valid data"
        print(f"  {subject.capitalize():<10} {display}")
    print()

    name, total = top_student(rows)
    if name:
        print(f"Top student: {name} with {total} valid marks")
    else:
        print("No students with valid data to rank.")

    issues = report_issues(rows)
    if issues:
        print("\nData issues found:")
        for issue in issues:
            print(f"  - {issue}")


def main():
    """Entry point. Load the CSV and print the summary."""
    try:
        rows = load_marks("marks_missing.csv")
    except FileNotFoundError:
        print("marks_missing.csv not found in the current folder.")
        return
    print_summary(rows)


if __name__ == "__main__":
    main()
