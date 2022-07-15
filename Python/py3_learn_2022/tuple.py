#lists that are ordered and cannot be changedf

student = ("Carlos",21,"male")
print(student.count("Carlos"))
print(student.index("male"))

for x in student:
    print(x)

if "Carlos" in student:
    print("Carlos is here")
