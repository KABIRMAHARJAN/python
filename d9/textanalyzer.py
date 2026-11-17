n=input("Enter a sentence: ")
print("TEXT ANALYZER:")

print(f"Orgianal text: {n}")
print(f"Total character: {len(n)}")
print(f"Total words: {len(n.split())}")
print(f"Upper case: {n.upper()}")
print(f"Lower case: {n.lower()}")
print(f"Reversed sentence: {n[::-1]}")
c=input("Enter a character to count: ")

print(f"The number of {c} is {n.lower().count(c.lower())}")