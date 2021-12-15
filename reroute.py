def dirReduc(arr):
    op = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    res = arr[:]
    i = 1
    while i < len(res):
        if res[i] == op[res[i - 1]]:
            res.pop(i - 1)
            res.pop(i - 1)
            i -= 2
        i += 1
        if i == 0:
            i += 1
    return res


a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(dirReduc(a), a)
