# st = {
#     "name":"Jagdish",
#     "email":"jagdish@gmail.com",
#     "lang" : ["guj","hin","eng"],
#     "hobbies":("cricket","football"),
#     "isMinore" : False,
#     "age" :22,
#     4j+5 : "abc",
#     "Name":"xyz"
# }

# print(st['name1'])
# print(st.get("name1"))
# print("continue...")
# print(st)

# print(st.keys())
# print(st.values())
# print(st.items())
# print(st)

# for i in st:
#     print(i)

# for i,j in st.items():
#     print(i,j)


person = {
    "name":"Chetan",
    "email":"chetan@gmial.com"
}

# person['name'] = 20
# person.setdefault("name","abc")
# print(person)

# person['name1'] = "xyz"
# person.update({"name":"abc","age":25})
# person.pop("name")
# person.popitem()

# person.clear()
# del person
# print(person)


student= {
    "st1" : {
        "name":"abc",
        "email":"abc@gmail.com"
    },
    "st2" :{
        "name":"xyz",
        "email":"xyz@gmail.com",
        "lang" : ["guj","hin","eng"]
    }
}

# print(student['st1']['name'])
# print(student['st2']['lang'][0])

# for i,j in student.items():
#     print(i)
#     for a,b in j.items():
#         print(a,b)