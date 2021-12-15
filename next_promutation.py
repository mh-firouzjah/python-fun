from itertools import permutations as permutations_fn
from timeit import default_timer

"""Algorithm L from Donald E. Knuth
کوچکترین بزرگترین ترکیب بعدی
پیاده‌سازی با حلقه‌ی وایل سرعت عمل ۱.۴ برابر بهتری نسبت به فور ارائه می‌دهد.
"""


def next_promutation(lst: list) -> list:
    """returns next promutation of a given list"""

    pivot = -1
    while True:
        if lst[pivot] < lst[pivot - 1]:
            pivot -= 1
            if pivot == -len(lst):
                return
        else:
            break

    left, right = lst[:pivot], lst[pivot:]
    inx = -1
    while True:
        if right[inx] < left[-1]:
            inx -= 1
        else:
            left[-1], right[inx] = right[inx], left[-1]
            break
    right = sorted(right)
    return left + right


start = default_timer()

test = list(range(10))
# test = [1, 2, 3]
# while res := next_promutation(test):
#     # print(res)
#     test = res
# print(res)

# [1, 2, 3] -> {
#     [1, 3, 2]
#     [2, 1, 3]
#     [2, 3, 1]
#     [3, 1, 2]
#     [3, 2, 1]
# }


def func(string: str):
    check_list = [r for tup in permutations_fn(string, len(string))
                  if (r := ''.join(tup)) > string]
    if check_list:
        return min(check_list)


# print('ab', ''.join(next_promutation(list('ab'))), 'ba')
print('ab', func('ab'), 'ba')
print('bb', next_promutation(list('bb')) is None)
# print('hefg', ''.join(next_promutation(list('hefg'))), 'hegf')
print('hefg', func('hefg'), 'hegf')
# print('dhck', ''.join(next_promutation(list('dhck'))), 'dhkc')
print('dhck', func('dhck'), 'dhkc')
# print('dkhc', ''.join(next_promutation(list('dkhc'))), 'hcdk')
print('dkhc', func('dkhc'), 'hcdk')


print(default_timer() - start)
