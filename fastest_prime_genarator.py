'''
this program is the fastest pythonic way genrates prime numbers
without need to 3rd party packages
'''
import time


def prime_generator(range_limit: int) -> list[int]:
    """
    Returns a list of prime numbers less than `n`.
    """

    from itertools import compress

    if range_limit <= 2:
        return []
    sieve = bytearray([True]) * (range_limit // 2)
    for i in range(3, int(range_limit ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = bytearray((range_limit - i * i - 1) // (2 * i) + 1)
    primes = list(compress(range(1, range_limit, 2), sieve))
    primes[0] = 2
    return primes

start_time = time.time()
prime_generator(10**8)  # time taken: ~=1.60 seconds
print("---- %s seconds ----" % (time.time()-start_time))
