sentence="python is easy and python is powerful"
word= sentence.split()
frequency={}

for x in word:
    if x in frequency:
        frequency[x]+=1
    else:
        frequency[x]=1

for word,count in frequency.items():
    print(word,":",count)