def func(li: list, a: int) -> int:
    if a == 1:
        return sum(li)
    queue = [[]]*a
    for index, item in enumerate(li):
        queue[index % a].append(item)
    tot = max(sum(queue[index]) for index in range(a))
    return tot


print(func([5, 3, 2], 1))
print(func([5, 3, 2], 2))
