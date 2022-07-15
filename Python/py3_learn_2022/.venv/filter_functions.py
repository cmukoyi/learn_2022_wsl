

friends = [("Rachel",12),
           ("Monica",18),
           ("Joey",98)]

age = lambda data:data[1] >= 18

drinking_buddies = list(filter(age,friends))
for i in drinking_buddies:
    print(i)
