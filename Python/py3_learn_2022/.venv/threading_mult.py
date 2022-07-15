# thread flow of execution

from ast import arg
import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")

def drink_tea():
    time.sleep(4)
    print("You drink tea")

def study():
    time.sleep(5)
    print("You study")

x = threading.Thread(target=eat_breakfast, args =())
x.start()

y = threading.Thread(target=drink_tea, args =())
y.start()

z = threading.Thread(target=study, args =())
z.start()

# thread sync
x.join()
y.join()
z.join()

# eat_breakfast()
# drink_tea()
# study()


print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())