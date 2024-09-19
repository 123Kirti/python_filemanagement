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
    def __init__(self, name, emailid, rollno, mark, student):
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

        with open("student_data.json", 'r+') as outfile:
            filedata = outfile.read()
            if filedata:
                outfile.seek(0)
                outfile.truncate()
                filedata = filedata[:-1] + ',' + json.dumps(d) + ']'
                outfile.write(filedata)
            else:
                outfile.write('[' + json.dumps(d) + ']')

    def view_records(filename):
        with open (filename, "r") as file:
            file_data = file.readlines()
            for text in file_data:
                print(text)

    def update_students():
        rollno = int(input("Enter roll number: "))
        try:
            with open("student_data.json", 'r') as file:
                students = json.load(file)
        except json.JSONDecodeError as err:
            print("Error: Unable to decode JSON file." , err)
            students = []

        for student in students:
            if student['rollno'] == rollno:
                print(f"Details of the student are: Name: {student['name']}, Email: {student['emailid']}, Roll Number: {student['rollno']}, Marks: {student['mark']}")

                student['name'] = input("Enter the name of the student: ") or student['name']
                student['emailid'] = input("Enter the emailid of the student: ") or student['emailid']

                while True:
                    subject = input("Write the subject whose marks need to be updated (or 'done' if none left): ")
                    if subject.lower() == 'done':
                        break
                    markss = input(f"Enter new marks for {subject}: ")
                    try:
                        student['mark'][subject] = int(markss)
                    except ValueError:
                        print("Enter a valid number.")
                        continue

                with open("student_data.json", 'w') as file:
                    json.dump(students, file, indent=4)
                print("Student record updated successfully.")
                return
        print("Student with the mentioned roll number not found.")

    def delete_student():
        rollno = int(input("Enter the student's roll number to be deleted: "))
        try:
            with open("student_data.json", 'r') as file:
                students = json.load(file)
        except json.JSONDecodeError:
            print("Error: Unable to decode JSON file.")
            students = []

        for i, student in enumerate(students):
            if student['rollno'] == rollno:
                print(f"Deleting {student['name']}'s record")
                del students[i]
                with open("student_data.json", 'w') as file:
                    json.dump(students, file, indent=4)
                print("Record deletion successful.")
                return
        print("Student with the mentioned roll number not found.")

    def search_student():
        name = input("Enter student's name: ")
        try:
            with open("student_data.json", 'r') as file:
                students = json.load(file)
        except json.JSONDecodeError as err:
            print("Error: Unable to decode JSON file." , err)
            students = []
        for student in students:
            if student['name'] == name:
                print(f"Details of the student are: Name: {student['name']}, Email: {student['emailid']}, Roll Number: {student['rollno']}, Marks: {student['mark']}")
                return
        print("Student with the mentioned name not found.")

        



def main():
    student = {}
    while True:
        print("Student Records")
        print("1. Add a Student Record")
        print("2. View Student Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Choose an Option: ")
        if choice == '1':
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

        elif choice== '2':
            Student.view_records("student_data.json")
            print("Viewing all student records.")
        elif choice == '3':
            Student.update_students()
        elif choice == '4':
            Student.delete_student()
        elif choice == '5':
            print("Searching.......")
            Student.search_student()
        elif choice == '6':
            print("Exiting......")
            break
        else:
            print("Invalid choice. Try Again.")

if __name__ == "__main__":
    main()

