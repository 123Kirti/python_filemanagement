'''
Basic File Operations
Objective: Develop a Python script for adding records to a file.
Tasks:
Define data structure for student records (name, email id, roll number, marks in subjects).
Write functions to add records to a file.
Test and validate file operations.
'''



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

            

        b = open("student.txt","r")
        bb = b.readlines()
        index = 0

        for x in bb:
            g = []
            g = bb[index]+','+"\n"
            print(g)
            with open ("student_data.json","a") as file:
                file.write(g)
            index+=1
    
#        with open ("student_data.json", "r") as file:
#            a = json.load(file)
#            a[rollno] = d

#            with open ("student_data.json","r") as getfile:
#                json.dump(a, getfile)





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


'''
def add_data():
    no = input("enter no ")
    name = input("enter name ")
    course = input("enter course ")

#    diction = {
#        "student no ": no,
#        "student name ": name,
#        "student course": course
#    }

    with open("student.txt", 'w') as file:
            d = {}
            d['no'] = no
            d['name'] = name
            d['course'] = course

            file.write(str(d))

            
    b = open("student.txt","r")
    bb = b.readlines()
    index = 0

    for x in bb:
        g = []
        g = bb[index]+','+"\n"
        print(g)
        with open ("student_data.json","a") as file:
            file.write(g)
        index+=1
    
add_data()
'''