from lazy import Queue_list
from heap import Queue_heap
import time
import matplotlib.pyplot as plt
import random

lazy = Queue_list()
heap = Queue_heap()


def test(arr, num):
    t = 0
    speed = []
    n = []
    for k in range(num):
        n.append(1000 * k)
        arr.qq = [random.randint(-100, 100) for i in range(1000 * k)]

        for i in range(10):
            time_begin = time.perf_counter()
            arr.insert(333)
            #arr.extractMax()
            t += time.perf_counter() - time_begin
        speed.append(t / 10)
    plt.plot(speed, n)
    plt.show()

test(lazy, 100)
test(heap, 100)
#plt.show()
