"""Print numbers via lock."""

import threading
import time

N = list(range(101))
LOCK = threading.Lock()
i = 0


def print_nums(con):
    """Print odd or even number."""
    global i
    while i < 101:
        with LOCK:
            if N and N[i] % 2 == con:
                print(N[i])
                time.sleep(0.01)
        i += 1
        time.sleep(0.1)


if __name__ == '__main__':
    t1 = threading.Thread(target=print_nums, args=(0,))
    t2 = threading.Thread(target=print_nums, args=(1,))
    t1.start()
    t2.start()
