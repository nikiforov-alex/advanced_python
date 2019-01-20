"""Print numbers via timer."""

import threading
import time

N = list(range(101))
i = 0


def print_nums(con):
    """Print odd or even number."""
    global i
    while i < 101:
        if N and N[i] % 2 == con:
            print(N[i])
        i += 1
        time.sleep(0.2)


if __name__ == '__main__':
    t1 = threading.Timer(0.05, function=print_nums, args=[0])
    t2 = threading.Timer(0.1, function=print_nums, args=[1])
    t1.start()
    t2.start()
