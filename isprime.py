import time

start_time = time.time()


def isprime(val: int) -> bool:
    if val in (2, 3):
        return True
    if val < 2 or val % 2 == 0:
        return False
    return all(val % num for num in range(3, int(val**0.5) + 1, 2))


print(isprime(11))  # time taken: ~=0.0 seconds
print("---- %s seconds ----" % (time.time() - start_time))
