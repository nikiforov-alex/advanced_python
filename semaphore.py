"""Print numbers via semaphore."""

import random
import threading
import time

N = list(range(101))
i = 0


def print_nums(con, s):
    """Print odd or even number."""
    global i
    while i < 101:
        s.acquire()
        if N and N[i] % 2 == con:
            print(N[i])
        i += 1
        time.sleep(random.uniform(0.01, 0.08))
        s.release()
        time.sleep(0.05)


if __name__ == '__main__':
    sem = threading.Semaphore()
    t1 = threading.Thread(target=print_nums, args=(0, sem))
    t2 = threading.Thread(target=print_nums, args=(1, sem))
    t1.start()
    t2.start()
