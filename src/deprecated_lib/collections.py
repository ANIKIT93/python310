from collections import Iterable


def print_instance():
    print(isinstance([1, 2, 3], Iterable))
    return True


if __name__ == "__main__":
    print_instance()
