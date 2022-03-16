import operator

dct = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
    '//': operator.floordiv
}


def func(string):
    for k in dct.keys():
        if k in string:
            return dct[k](int(string.split(k)[0]), int(string.split(k)[1]))


text = "1+(16+28)"


while '(' in text:
    inx = -1
    last = 0

    while text[inx] != '(':
        if text[inx] == ')':
            last = inx
        inx -= 1

    left = text[:inx]
    right = text[last + 1:] if last != -1 else ''

    text = f"{left}{func(text[inx + 1:last])}{right}"
    if '(' not in text:
        text = f"{func(text)}"
        break

print(text)
