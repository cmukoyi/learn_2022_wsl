
while True:
    name = input("Enter name : ")
    if name !="":
        break


phone_number = "125-8569-5632"
for i in phone_number:
    if i == "-":
        continue

    print(i, end="")

for j in range(1,21):
    if j == 13:
        pass
    else:
        print(j)
