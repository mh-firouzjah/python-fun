import time

start_time = time.time()


def isprime(val: int) -> bool:
    if val in (2, 3):
        return True
    if val < 2 or val % 2 == 0:
        return False
    for num in range(3, int(val**0.5)+1, 2):
        if val % num == 0:
            return False
    return True


def right_truncatable_primes() -> list[int]:
    # There are 27 restricted right_truncatable_primes:
    return [53, 317, 599, 797, 2393, 3793,
            3797, 7331, 23333, 23339, 31193, 31379, 37397,
            73331, 373393, 593993, 719333, 739397, 739399,
            2399333, 7393931, 7393933, 23399339, 29399999,
            37337999, 59393339, 73939133]


def shit_func(value: int) -> list[int]:
    rtp = right_truncatable_primes()
    return [it for it in rtp if len(str(it)) == value]


def func1(val: int) -> list[int]:
    bad_asses = list()
    for number in range(10**(val-1)+1, 10**val):
        num = number
        for _ in range(val):
            if not isprime(num):
                break
            num //= 10
        else:
            bad_asses.append(number)
    return bad_asses


def func2(val: int) -> list[int]:
    import re
    from itertools import product

    pattern = r'[2357][1379]{%d}' % (val-1)
    primes_below_10 = [2, 3, 5, 7]

    answer = []
    if val == 1:
        return primes_below_10
    combinations = list(product('123579', repeat=val))
    for combination in combinations:
        combination_str = ''.join(num for num in combination)
        check = re.search(pattern, combination_str)
        if check:
            num = int(combination_str)
            for _ in range(val):
                if not isprime(num):
                    break
                num //= 10
            else:
                answer.append(int(combination_str))

    return answer


def func3(val):
    if val == 1:
        return [2, 3, 5, 7]

    from itertools import product
    var1 = list(product('2357'))
    var2 = list(product('1379', repeat=val-1))
    var3 = list(product(var1, var2))
    var5 = []
    for item in var3:
        it = [''.join(''.join(i for i in it) for it in item)][0]
        num = int(it)
        for _ in range(val):
            if not isprime(num):
                break
            num //= 10
        else:
            var5.append(int(it))
    return var5


def func4(val):
    import re

    from fastest_prime_genarator import prime_generator
    pattern = r'[2357][1379]{%d}' % (val-1)
    lower_prime = prime_generator(10**(val-1))[-1]
    all_primes = prime_generator(10**val)
    primes = all_primes[all_primes.index(lower_prime):-1]
    res = list()
    for item in primes:
        check = re.search(pattern, str(item))
        if check:
            num = item
            for _ in range(val):
                if not isprime(num):
                    break
                num //= 10
            else:
                res.append(item)
    return res


def func5(val):
    from functools import reduce
    primes_below_10 = [2, 3, 5, 7]
    rest = [1, 3, 7, 9]
    result = [2]*val
    ans_list = list()
    if val == 1:
        return primes_below_10
    for num in primes_below_10:
        result[0] = num
        for index in range(1, val):
            step = 0
            while step < 4:
                result[index] = rest[step]
                step += 1
                current = reduce(lambda a, b: a*10+b, result[:index+1])
                if isprime(current):
                    print(current)
                    index += 1
                    step = 0
                    if index == val:
                        ans_list.append(current)
                        break
    return ans_list

# 23399339


# print(func1(7))  # time taken: ~=60 seconds
# print(func2(8))  # time taken: ~=5.35 seconds
# print(func3(8))  # time taken: ~=2.80 seconds
# print(func4(8))  # time taken: ~=8.60 seconds
# print(func5(8))  # time taken: ~=xxxx seconds
print(shit_func(8))
print("---- %s seconds ----" % (time.time()-start_time))
# [23399339, 29399999, 37337999, 59393339, 73939133]
