numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
           'eight', 'nine']

ops = {
    'plus': int.__add__,
    'times': int.__mul__,
    'minus': int.__sub__,
    'divided_by': int.__floordiv__
}


class number(object):
    def __init__(self, val) -> None:
        self.val = val

    def __call__(self, fn=None):
        if not fn:
            return self.val
        return fn[0](self.val, fn[1])


class operation(object):
    def __init__(self, name) -> None:
        self.name = name

    def __call__(self, operand: number):
        return ops[self.name], operand


for num, name in enumerate(numbers):
    globals()[name] = number(num)

# for k in ops.keys():
#     globals()[k] = operation(k)

# one = number(1)
# two = number(2)
# three = number(3)
# four = number(4)
# five = number(5)
# six = number(6)
# seven = number(7)
# eight = number(8)
# nine = number(9)

plus = operation('plus')
minus = operation('minus')
times = operation('times')
divided_by = operation('divided_by')

print(one(plus(two())))
print(nine())

# AmirSoroush solution
# numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
#            'eight', 'nine']

# operators = {'plus': '__add__', 'times': '__mul__', 'minus': '__sub__'}

# for num, name in enumerate(numbers):
#     globals()[name] = lambda o=None, t=num: \
#         getattr(t, o[0])(o[1]()) if o else t

# for k, v in operators.items():
#     globals()[k] = lambda n, t=v: (t, n)

# print(one(plus(two)))
