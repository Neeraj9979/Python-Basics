data=True
word="Neeraj"
line=1
with open("sample.txt","r") as f:
    data=f.readline()
    while data:
        if(word in data):
            print(f"{word} found at line no {line}")
            break
        line+=1