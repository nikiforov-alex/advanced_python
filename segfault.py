"""Script, which throw out SEGFAULT (SIGSEGV in Unix)."""
import resource


def recursive_func(i):
    """Sample recursive function."""
    recursive_func(i + 1)


if __name__ == '__main__':
    resource.setrlimit(resource.RLIMIT_STACK, [0, 1])
    recursive_func(0)
