'''
this program is made to check if an integer is perfect power or not
'''

import time

start_time = time.time()


def is_perfect_power(value: int) -> bool:
    '''
    check if value is perfect power and returns a booleian
    '''
    if value < 0:
        return False
    if value in (0, 1, 2, 3):
        return True
    sqrt = value**0.5
    if sqrt == int(sqrt):
        return False
    first_divisible = None
    for num in range(2, int(sqrt)+1):
        if value % num == 0:
            if not first_divisible:
                first_divisible = num
            elif num % first_divisible != 0:
                return False
    return True


print(is_perfect_power(360977247682932343357357))  # time taken: ~=0.0 seconds
print("---- %s seconds ----" % (time.time()-start_time))
