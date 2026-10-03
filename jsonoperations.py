import json
py_obj={
    "Name":"T.Neeraj",
    "Age":"19",
    "occupation":True,
    "Subject":["Python","ML","NLP","Deep learning"],
    "address":{
        "Town":"Bellampalli",
        "State":"Telanagana",
        "Country":"India"
    }
}
js_obj='{"Name":"T.Neeraj","Age":"19","occupation":true,"Subject":["Python","ML","NLP","Deep learning"],"address":{"Town":"Bellampalli","State":"Telanagana","Country":"India"} }'

js1_obj=json.dumps(py_obj)
print(type(js1_obj),js1_obj)

py1_obj=json.loads(js_obj)
print(type(py1_obj),py1_obj)

#Note:Loads is for loading json string into python string
#NOte:dumps is for converting python string into json string
#Note:' ' are very imortant for json string

with open("data1.json","r") as f:
    ans=json.load(f)
    print(type(ans),ans)

with open("data.json","w") as f1:
    ans1=json.dump(py_obj, f1)
    print(ans1)