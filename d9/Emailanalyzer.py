print("EMAIL ANALYZER")
email=input("Enter your email: ")

e=email.split("@",1)        
print(f"\nUsername: {e[0]}")
print(f"Domain: {e[1]}")
print(f"Ends with .com?: {email.endswith('.com')}")