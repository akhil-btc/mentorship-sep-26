class Student:
    def __init__(self, name):
        self.name = name
        self.marks = {}

    def add_mark(self, subject, score):
        """Add or update a subject mark for this student."""
        self.marks[subject] = score

    def total(self):
        """Return the sum of all subject marks."""
        return sum(self.marks.values())

    def average(self):
        """Return the average mark, or 0 if no marks."""
        if not self.marks:
            return 0
        return round(self.total() / len(self.marks), 2)

    def __str__(self):
        """Return a human-readable summary of this student."""
        return f"{self.name}: total={self.total()}, average={self.average()}"


shloka = Student("Shloka")
shloka.add_mark("math", 90)
shloka.add_mark("science", 88)
print(shloka)
# print(shloka.average())


a = [1, 2, 3]
print(a)