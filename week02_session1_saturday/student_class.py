"""
student_class.py — Week 2 OOP intro reference

The first proper Python class they'll write. Deliberately small: three
attributes, four methods, one __str__. Enough to make the pattern clear
without overwhelming.

Teaching arc for Block 3:
  1. Show why dicts run out of steam (all logic in loose functions)
  2. Introduce class as "data + behavior in one bundle"
  3. Live-code Student together
  4. Refactor analyze_marks to use Student (see analyze_marks_with_class.py)
"""


class Student:
    """Represents one student and their marks across subjects."""

    def __init__(self, name):
        """Create a new student with a name and an empty marks dictionary."""
        self.name = name
        self.marks = {}

    def add_mark(self, subject, score):
        """Add or update a subject mark for this student."""
        self.marks[subject] = score

    def total(self):
        """Return the sum of all subject marks."""
        return sum(self.marks.values())

    def average(self):
        """Return the average mark across all subjects, or 0 if none."""
        if not self.marks:
            return 0
        return round(self.total() / len(self.marks), 2)

    def subjects_below(self, threshold):
        """Return a list of subjects where this student scored below threshold."""
        return [subject for subject, mark in self.marks.items() if mark < threshold]

    def __str__(self):
        """Return a human-readable summary of this student."""
        return f"{self.name}: total={self.total()}, average={self.average()}"


def demo():
    """Small demo so they can see the class in action end-to-end."""
    shloka = Student("Shloka")
    shloka.add_mark("math", 90)
    shloka.add_mark("science", 88)
    shloka.add_mark("english", 85)
    shloka.add_mark("history", 82)
    shloka.add_mark("art", 91)

    shaurya = Student("Shaurya")
    shaurya.add_mark("math", 85)
    shaurya.add_mark("science", 78)
    shaurya.add_mark("english", 92)
    shaurya.add_mark("history", 74)
    shaurya.add_mark("art", 88)

    print(shloka)
    print(shaurya)
    print()
    print(f"Shloka's average: {shloka.average()}")
    print(f"Subjects Shaurya scored below 80 in: {shaurya.subjects_below(80)}")


if __name__ == "__main__":
    demo()
