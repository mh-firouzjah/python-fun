import string

'''Cleverest answer
def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - (ord('a')+1) for c in k))
'''


def high(strings):
    def _score(c):
        return string.ascii_lowercase.index(c) + 1
    li = [(sum(map(_score, word)), word)
          for word in strings.split()]
    m = sorted(li)[-1][0]
    for item in li:
        if item[0] == m:
            return item[1]


print(high('man i need a taxi up to ubud'))
