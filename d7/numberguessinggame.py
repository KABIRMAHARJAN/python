number = 9
print("Welcome to Number guess game.The number is in between 1-10")
print("Let's get started.")
a="y"
while a=="y":
        n=int(input("Enter your guess: "))

        if(n==number):
            print("Your guess was correct.")
            print("THANK YOU!!")
            break
        elif(n>number):
            print("Your guess is too high! Try again!")
            a=str(input("Do u want to continue(y/n): "))
        else:
            print("Your guess is too low! Try again!")
            a=input("Do u want to continue(y/n): ")


