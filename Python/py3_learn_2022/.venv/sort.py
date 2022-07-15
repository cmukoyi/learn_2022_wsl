# students = ("Carlos","Sean","Mike","Tupac","Luke","Admire")

# sorted_students = sorted(students,reverse=True)

# for i in sorted_students:
#     print(i)


students = [("Carlos","F",60),
            ("Sandy","A",33),
            ("Tupac","D",34),
            ("Mike","C",36)]

grade = lambda grades:grades[1]
students.sort(key=grade)

for i in students:
    print(i)

