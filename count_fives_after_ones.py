from functools import reduce

import numpy as np
from more_itertools import pairwise

t_list: list[int] = [1, 2, 3, 4, 5, 1, 4, 1, 5, 4, 1, 5]


def func1(lst: list[int]) -> int:
    return sum(1 for inx in range(1, len(lst))
               if (lst[inx - 1], lst[inx]) == (1, 5))


def func2(lst: list[int]) -> int:
    return sum(1 for item in zip(lst, lst[1:]) if item == (1, 5))


def func4(lst: list[int]) -> int:
    arr = np.array(list(zip(lst, lst[1:])))
    return np.where((arr[:, 0] == 1) & (arr[:, 1] == 5), 1, 0).sum()


def func5(lst: list[int]) -> int:
    return sum(map((1, 5).__eq__, zip(lst, lst[1:])))


def func6(lst: list[int]) -> int:
    func6.contr = 0

    def inner(x, y):
        func6.contr += (x, y) == (1, 5)
        return y
    reduce(inner, lst)
    return func6.contr


def func7(lst: list[int]) -> int:
    return sum(1 for item in pairwise(lst) if item == (1, 5))


# print(func1(t_list))
# print(func2(t_list))
# print(func3(t_list))
# print(func4(t_list))
# print(func5(t_list))
# print(func6(t_list))
print(func7(t_list))
