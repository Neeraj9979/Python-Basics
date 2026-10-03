info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

unique_course=set()
for name,course in info:
    unique_course.add(course)
    if(course=="English"):
        print(name)
print(unique_course)

dict_stu={}
for name,course in info:
    if(dict_stu.get(name)==None):
        dict_stu.update({name : list()})
        dict_stu[name].append(course)
    else:
        dict_stu[name].append(course)
print(dict_stu)

