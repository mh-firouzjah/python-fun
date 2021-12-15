from timeit import default_timer as timer


def test():
    i = 1
    while i < 5_790_000_001:
        if i / i == 2:
            print("Wonderful...")
        i += 1


if __name__ == '__main__':
    start = timer()
    test()
    print(f'Toke {timer()-start}')
