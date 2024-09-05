'''
Implementing CRUD Operations through CUI
Objective: Extend the CUI to support full CRUD operations and search functionality.
Tasks:
Implement functions for updating and deleting records.
Implement search functionality within the CUI.
Ensure data validation and error handling.
'''

import json
class Student:
    def __init__(self, name, emailid, rollno, mark,student):
        self.name = name
        self.emailid = emailid
        self.rollno = rollno
        self.mark = mark
        self.student = student

    def add_record(name, emailid, rollno, mark):
        with open("student.txt", 'a') as file:
            d = {}
            d['name'] = name
            d['emailid'] = emailid
            d['rollno'] = rollno
            d['mark'] = mark
            file.write(str(d))
            file.write(",\n")

        with open ("student_data.json","a+") as outfile:
            json.dump(d, outfile, indent=4)

    def view_records(filename):
        with open (filename, "r") as file:
            file_data = file.readlines()
            for text in file_data:
                print(text)

    def update_students():
        rollno = input("Enter roll number: ")
        with open("student_data.json",'r') as file:
                file_data = file.read()
                for student in file_data:
                    print(student)
                    if student['rollno'] == rollno:
                        student['name'] = input("Enter the updated name : ") or student['name']
                        student['emailid'] = input("Enter the updated emailid : ") or student['emailid']
        
                        while True:
                            subject = input ("Write the subject whose marks need to be updated (or 'done' if none left): ")
                            if subject.lower() == 'done':
                                break
                            markss = input(f"Enter new marks for {subject} : ")
                            try:
                                student['marks'][subject] = int(markss)
                            except ValueError:
                                print("Enter a valid number.")
                                continue
                print("Student record updated successfully.")
                return
        print("Student with the mentioned roll number not found.")
        
        
with open ("student_data.json","a") as outfile:
    outfile.write("[")

student = {}
while True:
    name = input("Student name : ")
    emailid = input("Email Id : ")
    rollno = int(input("Roll Number :"))
    mark = {}

    while True:
        subject = input("Enter subject : ")
        marks = int(input("Enter marks: "))
        try:
            mark[subject] = int(marks)
        except ValueError:
            print("Enter a valid number.")
            continue

        choice = input("Do you want to add more subjects ? [YES/NO] : ")
        if choice in ["NO","no"]:
            break

    Student.add_record(name,emailid, rollno, mark)
    student['name'] = name
    student['emailid']=emailid
    student['rollno']=rollno
    student['marks']=mark

    Choice = input("Do you want to enter more student records? [YES/NO] : ")
    if Choice in ["NO","no"]:
        break

with open ("student_data.json","a") as outfile:
    outfile.write("]")


while True:
    print("Student Records")
    print("1. Add a Student Record")
    print("2. View Student Records")
    print("4. Update Record")
    print("3. Exit")

    choice = input("Choose an Option: ")
    if choice == '1':
        continue
    elif choice== '2':
        Student.view_records("student_data.json")
        print("Viewing all student records.")
        break
    elif choice == '3':
        print("Exiing.")
        break
    elif choice == '4':
            Student.update_students()
    else:
        print("Invalid choice.Try Again.")






















































































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


def update_students(student):
    rollno = input("Enter roll number: ")
    for students in student:
        if students['rollno'] == rollno:
            print(f"Details of the student are:{students}")
            students['name'] = input("Enter the name of the student:") or students['name']
            students['emailid'] = input("Enter the emailid of the student: ") or students['emailid']
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