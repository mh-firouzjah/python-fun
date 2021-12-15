'''
Testing with n = 100: 21 should equal 24
Testing with n = 1000: 201 should equal 249
Testing with n = 100000: 20001 should equal 24999
Testing with n = 1000000000: 200000001 should equal 249999998
'''


def zeros(n):
    p, res = 0, 0
    while n > (5**p):
        p += 1
        res += n // pow(5, p)
    return res


print(zeros(0))
print(zeros(100))
print(zeros(1000))
print(zeros(10000))
print(zeros(1000000000))
