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
            for student in students:
                print(student)
    elif n==3:
        r=input("Enter roll no of student: ")
        c=0
        for x in students:
            if x["Roll no"]== r:
                print("Student found!!!")
                c+=1
                print(x)
                break

        if c==0:
            print("Not found!!")
    elif n==4:
        print("Exiting!!")
        break
    else:
        print("Invalid choice!!!")