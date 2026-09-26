import csv

from student_class import Student


SUBJECTS = ["math", "science", "english", "history", "art"]


def get_score(value):
    """Parse a raw CSV cell to int, or return None if it isn't valid."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def load_students(file_path):
    """Read the CSV and return a list of Student objects."""
    students = []
    with open(file_path, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row.get("name", "").strip()
            if not name:
                continue
            student = Student(name)
            for subject in SUBJECTS:
                score = get_score(row.get(subject, ""))
                if score is not None:
                    student.add_mark(subject, score)
            students.append(student)
    return students


def print_summary(students):
    """Print each student and the class-wide leaderboard."""
    print(f"Loaded {len(students)} students.\n")

    for student in students:
        print(student)
    print()

    if not students:
        print("No students to rank.")
        return

    top = max(students, key=lambda s: s.total())
    print(f"Top student: {top.name} with {top.total()} marks")


def main():
    """Entry point. Load the CSV and print the summary."""
    try:
        students = load_students("marks.csv")
    except FileNotFoundError:
        print("marks.csv not found in the current folder.")
        return
    print_summary(students)


if __name__ == "__main__":
    main()
