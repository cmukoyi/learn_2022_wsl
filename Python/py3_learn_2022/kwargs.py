
def hello(**kwargs):
    print("Hello "+ kwargs['first'] + " "+ kwargs['last'])
    print("hello ", end="")
    for key, value in kwargs.items():
        print(value, end="")

hello(first="Carlos ",title="Mr ",middle="Tupac ",last="Mukoyi ")