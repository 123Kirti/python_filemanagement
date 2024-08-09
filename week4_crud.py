'''
Implementing CRUD Operations through CUI
Objective: Extend the CUI to support full CRUD operations and search functionality.
Tasks:
Implement functions for updating and deleting records.
Implement search functionality within the CUI.
Ensure data validation and error handling.
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
        marks = {subject: int(mark) for subject, mark in marks.items()}
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
                try:
                    students.append(Student.from_string(line))
                except ValueError:
                    print("Skipping. Error while reading a line.")
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
        try:
            marks[subject] = int(markss)
        except ValueError:
            print("Enter a valid number.")
            continue
    return Student(name, emailid, rollno, marks)

def view_students(students):
    if not students:
        print("No student records found.")
    for student in students:
        print(f"Name: {student.name}, Email: {student.emailid}, Roll Number: {student.rollno}, Marks: {student.marks}")

def update_students(students):
    rollno = input("Enter roll number: ")
    for student in students:
        if student.rollno == rollno:
            print(f"Details of the student are:{student}")
            student.name = input("Enter the name of the student:") or student.name
            student.emailid = input("Enter the emailid of the student: ") or student.emailid
            while True:
                subject = input ("Write the subject whose marks need to be updated (or 'done' if none left): ")
                if subject.lower() == 'done':
                    break
                markss = input(f"Enter new marks for {subject} : ")
                try:
                    student.marks[subject] = int(markss)
                except ValueError:
                    print("Enter a valid number.")
                    continue
            print("Student record updated successfully.")
            return
    print("Student with the mentioned roll number not found.")

def delete_record(students):
    rollno = input("Enter the student's roll number to be deleted : ")
    for i, student in enumerate(students):
        if student.rollno == rollno:
            print(f"Deleting {student.name}'s record")
            del students[i]
            print("Record deletion successful.")
            return
    print("Student with the mentioned roll number not found.")

def search_student(students):
    searchby = input("Search by (name/ roll number/ email id): ").lower()
    searchvalue = input(f"Enter the {searchby} to search: ").lower()

    found = []
    for student in students:
        if searchby == "name" and student.name.lower() == searchvalue:
            found.append(student)
        elif searchby == "rollno" and student.rollno.lower() == searchvalue:
            found.append(student)
        elif searchby == "emailid" and student.email.lower() == searchvalue:
            found.append(student)

    if found:
        print(f"Found {len(found)} student(s):")
        for f in found:
            print(f"Name:{f.name}\n Email: {f.emailid}\n Roll Number:{f.rollno}\n Marks:{f.marks}")
    else:
        print(f"No student found with the given search name/rollno/emailid '{searchby}'")

def main():
    students = load_students('student.txt')
    while True:
        print("Student Records")
        print("1. Add a new Student")
        print("2. View Student record")
        print("3. Update Student record")
        print("4. Delete Student record")
        print("5. Search Student record")
        print("6. Save and Exit")
        print("7. Exit without Saving")

        choice = input("Choose an Option: ")
        if choice == '1':
            students.append(add_student())
        elif choice== '2':
            view_students(students)
        elif choice== '3':
            update_students(students)
        elif choice== '4':
            delete_record(students)
        elif choice== '5':
            search_student(students)
        elif choice == '6':
            save_students(students,'student.txt')
            print("Student record saved successfully.")
            break
        elif choice == '7':
            print("Exiing without saving.")
            break
        else:
            print("Invalid choice.Try Again.")

    
if __name__ == "__main__":
    main()

'''

class Student:
    def __init__(self, name, email, roll_number, marks):
        self.name = name
        self.email = email
        self.roll_number = roll_number
        self.marks = marks

    def __str__(self):
        marks_str = ",".join(f"{subject}:{mark}" for subject, mark in self.marks.items())
        return f"{self.name}|{self.email}|{self.roll_number}|{marks_str}"

    @classmethod
    def from_string(cls, data_str):
        name, email, roll_number, marks_str = data_str.strip().split("|")
        marks = dict(subject_mark.split(":") for subject_mark in marks_str.split(","))
        marks = {subject: int(mark) for subject, mark in marks.items()}
        return cls(name, email, roll_number, marks)


def save_students_to_file(students, filename):
    with open(filename, 'w') as file:
        for student in students:
            file.write(str(student) + "\n")


def load_students_from_file(filename):
    students = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    students.append(Student.from_string(line))
                except ValueError:
                    print("Error reading a line. Skipping.")
    except FileNotFoundError:
        print("File not found. Starting with an empty record.")
    return students


def add_student():
    name = input("Enter student's name: ")
    email = input("Enter student's email: ")
    roll_number = input("Enter student's roll number: ")
    marks = {}
    while True:
        subject = input("Enter subject name (or 'done' to finish): ")
        if subject.lower() == 'done':
            break
        mark = input(f"Enter marks for {subject}: ")
        try:
            marks[subject] = int(mark)
        except ValueError:
            print("Invalid input for marks. Please enter a valid number.")
            continue
    return Student(name, email, roll_number, marks)


def view_students(students):
    if not students:
        print("No student records available.")
    for student in students:
        print(f"Name: {student.name}, Email: {student.email}, Roll Number: {student.roll_number}, Marks: {student.marks}")


def update_student(students):
    roll_number = input("Enter the roll number of the student to update: ")
    for student in students:
        if student.roll_number == roll_number:
            print(f"Current details: {student}")
            student.name = input(f"Enter new name (current: {student.name}): ") or student.name
            student.email = input(f"Enter new email (current: {student.email}): ") or student.email
            while True:
                subject = input("Enter subject name to update marks (or 'done' to finish): ")
                if subject.lower() == 'done':
                    break
                mark = input(f"Enter new marks for {subject}: ")
                try:
                    student.marks[subject] = int(mark)
                except ValueError:
                    print("Invalid input for marks. Please enter a valid number.")
                    continue
            print("Student updated successfully.")
            return
    print("Student with the given roll number not found.")


def delete_student(students):
    roll_number = input("Enter the roll number of the student to delete: ")
    for i, student in enumerate(students):
        if student.roll_number == roll_number:
            print(f"Deleting student: {student}")
            del students[i]
            print("Student deleted successfully.")
            return
    print("Student with the given roll number not found.")


def search_students(students):
    criterion = input("Search by (name/email/roll_number): ").lower()
    value = input(f"Enter the {criterion} to search for: ").lower()
    
    found_students = []
    for student in students:
        if criterion == "name" and student.name.lower() == value:
            found_students.append(student)
        elif criterion == "email" and student.email.lower() == value:
            found_students.append(student)
        elif criterion == "roll_number" and student.roll_number.lower() == value:
            found_students.append(student)
    
    if found_students:
        print(f"\nFound {len(found_students)} student(s):")
        for student in found_students:
            print(f"Name: {student.name}, Email: {student.email}, Roll Number: {student.roll_number}, Marks: {student.marks}")
    else:
        print("No students found with the given criteria.")


def main():
    students = load_students_from_file('studentss.txt')
    
    while True:
        print("\n--- Student Records Management ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Students")
        print("6. Save and Exit")
        print("7. Exit without Saving")
        choice = input("Choose an option: ")
        
        if choice == '1':
            students.append(add_student())
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            update_student(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            search_students(students)
        elif choice == '6':
            save_students_to_file(students, 'studentss.txt')
            print("Students saved successfully. Exiting.")
            break
        elif choice == '7':
            print("Exiting without saving.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
'''