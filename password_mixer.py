"""
persian text ->
اگر یک عدد رمز وارد شود ممکن است با عددی در بالا، پایین، چپ و یا راست خود عوض شود.
"""
from itertools import product


def fn(n):
    dic = {
        1: '124',
        2: '1235',
        3: '236',
        4: '1457',
        5: '24568',
        6: '3569',
        7: '478',
        8: '57890',
        9: '689'}
    li = list(product(*[dic[int(c)] for c in str(n)], repeat=1))
    return [''.join(t for t in tup) for tup in li]


print(fn(8))
print(fn(11))
print(fn(369))
print(fn(368))
