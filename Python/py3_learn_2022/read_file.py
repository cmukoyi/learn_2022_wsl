try:
    with open('test.txt') as file:
        print(file.read())
        print(file.closed)
except FileNotFoundError as e:
    print(e)
    print("That file was not found")
    
