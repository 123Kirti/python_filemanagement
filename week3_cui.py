'''
Command-Line User Interface (CUI)
Objective: Create a CUI for taking input and performing basic operations.
Tasks:
Design a simple CUI for user interaction.
Implement input functions to capture data.
Connect CUI with file handling functions.
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
            outfile.write(",\n")
   
        
        
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
        mark[subject] = marks
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




def view_records(filename):
    with open (filename, "r") as file:
        file_data = file.readlines()
        for text in file_data:
            print(text)


while True:
    print("Student Records")
    print("1. Add a Student Record")
    print("2. View Student Records")
    print("3. Exit")

    choice = input("Choose an Option: ")
    if choice == '1':
        continue
    elif choice== '2':
        view_records("student_data.json")
        print("Viewing all student records.")
        break
    elif choice == '3':
        print("Exiing.")
        break
    else:
        print("Invalid choice.Try Again.")