contacts = {
    "number":4,
    "students":
    [
        {"name:":"Chris Romulus", "email":"chris@romuluslab.com"},
        {"name":"Marlon Romulus", "email":"marlon@romuluslab.com"},
        {"name":"Blake Romulus", "email":"blake@romuluslab.com"},
        {"name":"Gerard Romulus", "email":"gerard@romuluslab.com" }
    ]
}

for student in contacts["students"]:
    print(student["email"])