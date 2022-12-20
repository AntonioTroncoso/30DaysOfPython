dog = dict()
dog = {"name": "Huski", "color": "White", "breed": "bulldog", "legs": 4, "age": 2}
student_dictionary = {
    "first_name": "Antonio",
    "last_name": "Troncoso",
    "gender": "M",
    "age": 17,
    "marital_status": "unmarried",
    "skills": ["procrastinating"],
    "country": "Spain",
    "city": "Jerez",
    "address": "lol",
}
print(len(student_dictionary))
print(student_dictionary["skills"])
print(type(student_dictionary["skills"]))
student_dictionary["skills"].append("Sleeping")
list_keys = list(student_dictionary.keys())
list_values = list(student_dictionary.values())
list_of_tuples = [(k, v) for k, v in student_dictionary.items()]
student_dictionary.pop("marital_status")
del dog
