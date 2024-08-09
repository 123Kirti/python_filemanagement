'''
Command-Line User Interface (CUI)
Objective: Create a CUI for taking input and performing basic operations.
Tasks:
Design a simple CUI for user interaction.
Implement input functions to capture data.
Connect CUI with file handling functions.
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
    
def save_students(students, filename):
    with open(filename, 'w') as file:
        for student in students:
            file.write(str(student)+"\n")

def load_students(filename):
    students = []
    try:
        with open(filename,'r') as file:
            for line in file:
                students.append(Student.from_string(line))
    except FileNotFoundError:
        print("File not found. Starting with an empty record.")
    return students
    

def add_student():
    name = input("Name : ")
    emailid = input("Email Id : ")
    rollno = input ("Roll Number : ")
    marks = {}

    while True:
        subject = input ("Subject Name (if all done write 'done') : ")
        if subject.lower() == 'done':
            break
        markss = input(f"Marks for {subject} : ")
        marks[subject] = markss
    return Student(name, emailid, rollno, marks)

def view_students(students):
    if not students:
        print("No student records found.")
    for student in students:
        print(f"Name: {student.name}, Email: {student.emailid}, Roll Number: {student.rollno}, Marks: {student.marks}")

def main():
    students = load_students('student.txt')
    while True:
        print("Student Records")
        print("1. Add Student")
        print("2. View Student")
        print("3. Save and Exit")
        print("4. Exit without saving")

        choice = input("Choose an Option: ")
        if choice == '1':
            students.append(add_student())
        elif choice== '2':
            view_students(students)
        elif choice == '3':
            save_students(students,'student.txt')
            print("Student record saved successfully.")
            break
        elif choice == '4':
            print("Exiing without saving.")
            break
        else:
            print("Invalid choice.Try Again.")

    
if __name__ == "__main__":
    main()

