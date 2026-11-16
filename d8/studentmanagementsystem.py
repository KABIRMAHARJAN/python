students=[]
while True:
    print("STUDENT MANAGEMENT SYSTEM")
    print("1.Add student")
    print("2.Display student")
    print("3.Search student")
    print("4.Exit")
    n=int(input("Enter your choice: "))
    if n==1:
        name=input("Enter name:")
        roll=input("Enter roll:")
        grade=int(input("Enter grade:"))
        student={
            "Name": name,
            "Roll no": roll,
            "Grade": grade,
        }
        students.append(student)
    elif n==2:
        if len(students)==0:
            print("No records found!!")
        else:
            print(students)
    elif n==3:
        r=input("Enter roll no of student: ")
        for x in students:
            if r == "Roll no" in x:
                print (students)
            else:
                print("Student not found!!")
    elif n==4:
        print("Exiting!!")
        break