# number = lambda x: lambda f=lambda x: x: f(x)
# zero,one,two,three,four,five,six,seven,eight,nine = map(number,range(10))
# plus = lambda x: getattr(x, '__add__'),
# minus = lambda x: getattr(x, '__sub__'),
# times = lambda x: getattr(x, '__mul__'),
# divided_by = lambda x: getattr(x, '__floordiv__')

def number(x: int) -> function:
    def identity(x: int) -> int: return x

    def inner(fn: function = identity) -> int:
        return fn(x)
    return inner


zero, one, two, three, four, five, six, seven, eight, nine = map(
    number, range(10))


def plus(x) -> function: return getattr(x, '__add__')
def minus(x) -> function: return getattr(x, '__sub__')
def times(x) -> function: return getattr(x, '__mul__')
def divided_by(x) -> function: return getattr(x, '__floordiv__')


print(one(plus(two())))
