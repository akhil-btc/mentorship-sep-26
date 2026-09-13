class Classroom:
    def __init__(self, name):
        self.name = name
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    

    def subject_averages(self):
        totals = {}
        counts = {}
        for student in self.students:
            for subject, mark in student.marks.items():
                totals[subject] = totals.get(subject, 0) + mark
                counts[subject] = counts.get(subject, 0) + 1
        return {
            subject: round(totals[subject] / counts[subject], 2)
            for subject in totals
        }
    def __str__(self):
        """Return a human-readable summary of this student."""
        return f"{self.name}: nmae={self.name}, students={self.students}"
    

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
        return f"{self.name}: total={self.name}, average={self.marks}"

classroom = Classroom("AI")
print(classroom)
shloka = Student("Shloka")
shaurya = Student("Shaurya")

classroom.add_student(shloka)
classroom.add_student(shaurya)

print(classroom)








student - name and marks

clasroom with students

[[]]


calculate the area of shapes - rectange , square, circle

class Shape




class rectangle, class saueare, class circle


data = l b, square = a, cicle- radius




