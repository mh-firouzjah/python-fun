"""Algorithm L from Donald E. Knuth
کوچکترین بزرگترین ترکیب بعدی از یک رشته را برمیگرداند.
"""


def next_promutation(string: str) -> str:
    """returns next promutation of a given string"""
    lst = list(string)

    if lst == sorted(lst, reverse=True):
        return 'no answer'

    pivot = - 1
    while lst[pivot] <= lst[pivot - 1]:
        pivot -= 1

    # left, right = lst[:pivot], lst[pivot:]  # 29357632 -> [2935], [7632]

    inx = - 1
    while lst[inx] <= lst[pivot - 1]:
        inx -= 1

    # left[-1], right[inx] = right[inx], left[-1]  # [2936], [7532]
    lst[pivot - 1], lst[inx] = lst[inx], lst[pivot - 1]  # [2936], [7532]

    # right.sort()  # [2936], [2357]
    lst[pivot:] = sorted(lst[pivot:])  # [2936], [2357]

    # return ''.join(left + right)
    return ''.join(lst)


print(next_promutation('29357632'))

# def func(string: str):
#     from itertools import permutations as permutations_fn
#     check_list = [promut for tup in permutations_fn(string, len(string))
#                   if (promut := ''.join(tup)) > string]
#     if check_list:
#         return min(check_list)

# loop = int(input())
# strings = [next_promutation(input()) for _ in range(loop)]
# for item in strings:
#     print(item)
