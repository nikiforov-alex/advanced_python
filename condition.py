"""Print numbers via condition."""

import random
import threading
import time

NUMS = list(range(101))


def print_nums(con, cv):
    """Print odd or even number."""
    i = 0
    while i < 101:
        with cv:
            if NUMS and NUMS[i] % 2 == con:
                print(NUMS[i])
            i += 1
            cv.notify()
            time.sleep(0.05)
        time.sleep(random.uniform(0.05, 0.08))


if __name__ == '__main__':
    cond = threading.Condition()
    t1 = threading.Thread(target=print_nums, args=(0, cond))
    t2 = threading.Thread(target=print_nums, args=(1, cond))
    t1.start()
    t2.start()
