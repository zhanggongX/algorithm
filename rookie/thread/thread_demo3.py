import random
from time import sleep
import _thread as thread


def fun(a, b):
    print(a, b)
    sleep(random.randint(1, 5))
    print('break')


for i in range(8):
    sleep(1)
    thread.start_new_thread(fun, (i + 1, 'a' * (i + 1)))

input()
