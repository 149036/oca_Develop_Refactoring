import random


def print_random():
    list_100 = [random.randint(0, 100000001) for _ in range(100)]
    list_100_000_000 = [random.randint(0, 100000001) for _ in range(1000000)]
    set_100_000_000 = set(list_100_000_000)
    result = [data for data in set_100_000_000 if data in list_100]

    print(result)


if __name__ == "__main__":
    print_random()
