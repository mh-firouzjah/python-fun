from itertools import permutations as prm


def permutations(string):
    return list(dict.fromkeys([''.join(it) for it in prm(string)]))


print(permutations('aabb'))
print(permutations('a'))
print(permutations('ab'))
