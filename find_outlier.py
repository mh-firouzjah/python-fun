def find_outlier(integers):
    res = int()

    def _remember(x):
        nonlocal res
        res = x
        return True
    if sum(i % 2 for i in integers[:3]) >= 2:
        any(i % 2 == 0 and _remember(i) for i in integers)
    else:
        any(i % 2 and _remember(i) for i in integers)
    return res


l1 = [2, 4, 0, 100, 4, 11, 2602, 36]
l2 = [160, 3, 1719, 19, 11, 13, -21]
l3 = [3, 1719, 19, 11, 13, 160, -21]

print(find_outlier(l1))
print(find_outlier(l2))
print(find_outlier(l3))
