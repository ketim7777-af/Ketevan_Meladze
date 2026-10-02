student_profile = {
    "contacts": {
        "name": "Anna",
        "e-mail": "anna@gmail.com",
        "mobile": 577400300
    },
    "courses": {
        "python": {
            "score": 65,
            "passed": True
        },
        "web": {
            "score": 40,
            "passed": False
        }
    }  
}

print(student_profile["contacts"]["e-mail"])
print(student_profile["courses"]["python"]["score"])

student_profile["courses"]["web"]["score"] = 65
print(student_profile["courses"]["web"]["score"])

student_profile["courses"]["web"]["passed"] = True
print(student_profile["courses"]["web"]["passed"])

student_profile["contacts"].pop("mobile")

print(student_profile["courses"]["web"])
print(student_profile["contacts"])
print(student_profile["contacts"].get("mobile", "mobile number does not exist"))


