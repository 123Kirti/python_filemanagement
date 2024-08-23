'''
Basic File Operations
Objective: Develop a Python script for adding records to a file.
Tasks:
Define data structure for student records (name, email id, roll number, marks in subjects).
Write functions to add records to a file.
Test and validate file operations.
'''

import json
class Student:
    def __init__(self, name, emailid, rollno, mark):
        self.name = name
        self.emailid = emailid
        self.rollno = rollno
        self.mark = mark

    def add_record(name, emailid, rollno, mark):
        with open("student.txt", 'a') as file:
            d = {}
            d['name'] = name
            d['emailid'] = emailid
            d['rollno'] = rollno
            d['mark'] = mark
            file.write(str(d))
            file.write(",\n")

        def json_dump():
            with open ("student.txt","r") as files:
                json_object = json.dumps(d, indent= 4)
                with open ("student_data.json","a") as outfile:
                    outfile.write(json_object)
                    outfile.write(",\n")
        json_dump()
        
        
with open ("student_data.json","a") as outfile:
    outfile.write("[")

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

    Choice = input("Do you want to enter more student records? [YES/NO] : ")
    if Choice in ["NO","no"]:
        break

with open ("student_data.json","a") as outfile:
    outfile.write("]")