"""
Given two functions `f` and `g` and a list `M` with the following conditions:
- f(g(x)) = x, g(f(x)) = x
- l1 = list(map(f, L))
- l2 = list(map(g, L))
- random.shuflle(l1)
- random.shuflle(l2)
- M = l1 + l2

create a function which returns the Original `L` which is a list of integers.
"""

# f(g(x)) = x => fog(x) = x
# L = [a, b] => M = [f(a), f(b), g(a), g(b)]
# map(f, M) -> [f(f(a)), f(f(b)), f(g(a)), f(g(b))] ->
# [fof(a), fof(b), a, b]


L = [9, 25]


def f(x): return x**2
def g(x): return x**(1 / 2)


M = [f(x) for x in L] + [g(x) for x in L]


def func(f, g, M):
    return [x for x in map(f, M) if f(x) in M]
    # return [x for x in map(g, M) if g(x) in M]
    # return [x for x in map(g, M) if f(x) in M]
    # return [x for x in map(f, M) if g(x) in M]


print(func(f, g, M))
