from timeit import default_timer

arr = [[0] * 1000] * 1000

res = 0

ts = default_timer()
for i in range(1000):
    for j in range(1000):
        if arr[i][j] > 0:
            res += 1
print(f"took: {default_timer() - ts}s")

ts = default_timer()
for i in range(1000):
    for j in range(1000):
        if arr[j][i] > 0:
            res += 1
print(f"took: {default_timer() - ts}s")

ts = default_timer()
_ = [(res := res + 1) for i in range(1000)
     for j in range(1000) if arr[i][j] > 0]
print(f"took: {default_timer() - ts}s")

ts = default_timer()
_ = [(res := res + 1) for i in range(1000)
     for j in range(1000) if arr[j][i] > 0]
print(f"took: {default_timer() - ts}s")

ts = default_timer()
_ = [(res := res + 1) if arr[j][i] > 0 else res for i in range(1000)
     for j in range(1000)]
print(f"took: {default_timer() - ts}s")
