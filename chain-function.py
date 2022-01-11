# q1
# def func(lst: list) -> tuple[list, list]:
#     l1, l2 = [], []
#     for it in lst:
#         if it % 2:
#             l2.append(it)
#         else:
#             l1.append(it)
#     return (l1, l2)

# q2
# print(' '.join(
#     sorted([ch if not (ord(ch) - 97) % 2 else ch.upper() for ch in input()],
#            reverse=True)))

# q3
class Chain(object):

    def __init__(self, arg):
        if not isinstance(arg, (str, int, float)):
            raise Exception("Invalid operation")
        self.arg = arg

    def __call__(self, v):
        if not isinstance(self.arg, type(v)):
            raise Exception("Invalid operation")
        if isinstance(self.arg, (float, int)):
            return Chain(self.arg + v)
        if isinstance(self.arg, str):
            return Chain(self.arg + ' ' + v)
        raise Exception("Invalid operation")

    def __repr__(self) -> str:
        return f"{self.arg}"

    def __eq__(self, __o: object) -> bool:
        return self.arg == __o
print(Chain(2.1))
print(Chain(2) == 2)
print(Chain(2)(3))
print(Chain(2)(3)(1))
print(Chain("abc")(2))
print(Chain("abc")("def"))
print(Chain("abc")(["def"]))
