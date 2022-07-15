animal = "cow"
item = "moon"

#print("The {0} jumped over the {1}".format(animal,item))
#print("The {} jumped over the {}".format(animal,item)) #keywaord args
text = "The {} jumped over the {}"
print(text.format(animal,item))

name = "Carlos"
print("Hello, my name is {:10}. Nice to meet you".format(name))
print("Hello, my name is {:^10}. Nice to meet you".format(name))

number = 1000

print("The number pi is {:.3f}".format(number))
print("The number pi is {:,}".format(number))
print("The number pi is {:b}".format(number))
print("The number pi is {:o}".format(number))
print("The number Hex is {:X}".format(number))
print("The number Sci is {:E}".format(number))



