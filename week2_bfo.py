'''
Basic File Operations
Objective: Develop a Python script for adding records to a file.
Tasks:
Define data structure for student records (name, email id, roll number, marks in subjects).
Write functions to add records to a file.
Test and validate file operations.
'''

class Student:
    def __init__(self, name, emailid, rollno, marks):
        self.name = name
        self.emailid = emailid
        self.rollno = rollno
        self.marks = marks

    def __str__(self):
        marks_str = ",".join(f"{subject}:{mark}" for subject, mark in self.marks.items())
        return f"{self.name}->{self.emailid}->{self.rollno}->{marks_str}"
    
    @classmethod
    def from_string(cls, data_str):
        name, emailid, rollno, marks_str = data_str.strip().split("->")
        marks = dict(subject_mark.split(":") for subject_mark in marks_str.split(","))
        return cls(name, emailid, rollno, marks)
    
def save_students_to_file(students, filename):
    with open(filename, 'w') as file:
        for student in students:
            file.write(str(student)+"\n")

def load_students_from_file(filename):
    students = []
    with open(filename,'r') as file:
        for line in file:
            students.append(Student.from_string(line))
    return students
    
students = [
    Student('Kirti','kirti@gmail.com','123',{'Mathematics':96, 'Science':90}),
    Student('Anvesha','anvesha@gmail.com','124',{'Mathematics':98, 'Science':92}),
    Student('Anubhav','anubhav@gmail.com','123',{'Mathematics':95, 'Science':99})
]

save_students_to_file(students, 'students.txt')
loaded_Students = load_students_from_file('students.txt')

for student in loaded_Students:
    print(f"Name: {student.name}, Email: {student.emailid}, Roll Number: {student.rollno}, Marks: {student.marks}")