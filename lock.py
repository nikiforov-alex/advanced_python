"""Print numbers via lock."""

import multiprocessing
import time

N = list(range(101))
LOCK = multiprocessing.Lock()
i = 0


def print_nums(con):
    """Print odd or even number."""
    global i
    while i < 101:
        with LOCK:
            if N and N[i] % 2 == con:
                print(N[i])
                time.sleep(0.05)
        i += 1
        time.sleep(0.05)


if __name__ == '__main__':
    t1 = multiprocessing.Process(target=print_nums, args=(0,))
    t2 = multiprocessing.Process(target=print_nums, args=(1,))
    t1.start()
    t2.start()
