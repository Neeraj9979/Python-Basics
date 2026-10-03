info={
    "Name":"T.Neeraj",
    "Age":19,
    "City":"Bellampalli",
    "Hobbies":["Coding","Learnig","Speak"],
}
print(info.keys())
print(info.values())
print(info.items())
print(info.get("Age1"))
info.update({                        #Similar to the list .append()
    "Occupation":"Ai-Engineer"
})
print(info)
