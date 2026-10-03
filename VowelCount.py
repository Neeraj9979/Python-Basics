word="artificial"
count=0
for ch in word:
    if(ch=="a" or ch=="e"or ch=="i"  or ch=="o" or ch=="u"):
        count+=1
print("Count is:",count)

# Using Memership Operator

word="Artificial Intelligence"
counts=0
for w in word:
    if(w in "aeiou"):
        counts+=1
print(f"Final Count of vowels is:{counts}")
