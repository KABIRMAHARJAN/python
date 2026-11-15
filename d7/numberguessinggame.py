number = 9
print("Welcome to Number guess game.The number is in between 1-10. Only 5 chances are given to guess the number.")
print("Let's get started.")
c=0
while(c<5):
    c+=1
    n=int(input("Enter your guess: "))
    if(n==number):
        print("Your guess was correct.")
        print("THANK YOU!!")
        break
    elif(n>number):
        print("Your guess is too high! Only",5-c,"attempts left. Try again!")
    else:
        print("Your guess is too low! Only",5-c,"attempts left. Try again!")
    
else:
    print("No attempts left. The number was",number)