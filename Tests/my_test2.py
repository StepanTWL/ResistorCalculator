from threading import Thread
from time import sleep
def func():
    while True:
        print(f"from child thread: 0")
        sleep(0.5)
th = Thread(target=func)
th.start()
while True:
    print(f"from main thread: 0")
    sleep(1)

