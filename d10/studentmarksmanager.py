students=[]

while True:
    print("STUDENTS MARKS MANAGER")
    print("\n1. Add Students Marks")
    print("2. Display All Marks")
    print("3. Calculate Average")
    print("4. Find Highest")
    print("5. EXIT")
    c=input("Enter your choice: ")


    match c:
        case "1":
            a="y"
            while a=="y":
                name=input("Enter student name: ")
                marks=float(input("Enter marks: "))
                student=[name,marks]
                students.append(student)
                a=input("Do u want to add another student(y/n): ")
        case "2":
            if len(students)==0:
                print("No records found!!")
            else:
                for x,y in students:
                    print(x,":",y)
        case "3":
            if len(students)==0:
                print("No records found!!")
            else:
                total = 0
                n=0
                for x,y in students:
                    total=y+total
                    n=n+1
                print(f"Average Marks of all students is {total/n}")
        case "4":
            if len(students)==0:
                print("No records found!!")
            else:
                max=students[0]
                for student in students:
                    if student[1]>max[1]:
                        max = student
                
                print("Highest marks is : ")
                print(max[0],":",max[1])
        case "5":
            print("EXITING!!")
            break
        case _:
            print("Invalid choice!!")