def func1() -> str:
    lst = input().split()
    a, b = map(int, input().split(','))
    l1 = lst[:a - 1]
    l2 = lst[a - 1:b]
    l3 = lst[b:]
    return ' '.join(l1 + l2[::-1] + l3)


def func2(n: int) -> str:
    st = str(n)
    if list(st) == sorted(st):
        for i in st[1:]:
            if int(st[0]) % 2 != int(i) % 2:
                return "No"
        else:
            return "Yes"
    return "No"


def func3():
    cn = int(input())
    lst = []
    for _ in range(cn):
        lst.append(list(map(int, input().split())))
    go = list(map(int, input().split(',')))

    togo = list(zip(go, go[1:]))
    togo += [it[::-1] for it in togo[::-1]]
    price = 0
    for i, t in enumerate(togo):
        price += lst[t[0]][t[1]] - (lst[t[0]][t[1]] * (i + 1)) // 100
    return price


print(func3())
