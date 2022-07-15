from typing import Text


try:
    text = "\nThis will append some text"
    with open('test.txt','a') as file:
        file.write(text)
except Exception as e:
    print(e)