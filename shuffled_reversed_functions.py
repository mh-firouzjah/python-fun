import math
import random

L = [1, 4, 9, 16, 25, 36, 49, 64, 81]

def f(x): return math.pow(x, 2)
def g(x): return int(math.sqrt(x))

l1 = [f(x) for x in L]
# [1, 16, 81, 256, 625, 1296, 2401, 4096, 6561]

l2 = [g(x) for x in L]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(l1, l2)

random.shuffle(l1)
random.shuffle(l2)
M = l1 + l2

l3 = []
l4 = []
l6 = []
for x in M:
    l3.append(f(x))
    l4.append(g(x))
me = set(l3) & set(l4)
mm = set(map(f, M)) & set(map(g, M))
print(me == set(L))
print(M)
