"""Print numbers via event."""

import threading
import time

N = list(range(101))


def print_nums(con, e):
    """Print odd or even number."""
    i = 0
    while i < 101:
        if e.isSet():
            e.wait()
        if N and N[i] % 2 == con:
            print(N[i], )
        i += 1
        e.clear()
        time.sleep(0.05)
        e.set()


if __name__ == '__main__':
    event = threading.Event()
    t1 = threading.Thread(target=print_nums, args=(0, event))
    t2 = threading.Thread(target=print_nums, args=(1, event))
    t1.start()
    t2.start()
