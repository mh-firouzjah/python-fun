import math
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


def destruct(num: int) -> list[int]:
    sqrt = math.sqrt(num)
    primes = prime_generator(int(sqrt))
    res = list()
    for prime in primes:
        if not num % prime:
            res.append(prime)
    return res


print("destruct(11248985632788451)")
start_time = time.time()
print(destruct(11248985632788451))
print("---- %s seconds ----" % (time.time()-start_time))

print("destruct(1245547123454123)")
start_time = time.time()
print(destruct(1245547123454123))
print("---- %s seconds ----" % (time.time()-start_time))

print("destruct(21784567140200225)")
start_time = time.time()
print(destruct(21784567140200225))
print("---- %s seconds ----" % (time.time()-start_time))

print("destruct(188155647450620685)")
start_time = time.time()
print(destruct(188155647450620685))
print("---- %s seconds ----" % (time.time()-start_time))

print("destruct(6116516165165)")
start_time = time.time()
print(destruct(6116516165165))
print("---- %s seconds ----" % (time.time()-start_time))

'''
Result

destruct(11248985632788451)
[]
---- 2.133331775665283 seconds ----

destruct(1245547123454123)
[7, 69833]
---- 0.6982822418212891 seconds ----

destruct(21784567140200225)
[5]
---- 2.91977858543396 seconds ----

destruct(188155647450620685)
[3, 5, 11, 1579, 95063, 2532319]
---- 8.536773920059204 seconds ----

destruct(6116516165165)
[5, 7, 21089]
---- 0.054852962493896484 seconds ----

total of 14.4s
'''
