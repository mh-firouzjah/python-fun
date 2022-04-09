def mix(s1, s2):
    from collections import Counter

    s1 = Counter(''.join(filter(str.islower, s1)))
    s2 = Counter(''.join(filter(str.islower, s2)))
    dct = s1 | s2
    dct = {k: v for k, v in dct.items() if v > 1}
    def sign(a, b): return '=' if a == b else '1' if a > b else '2'

    lst = sorted([f'{sign(s1.get(k, 0), s2.get(k, 0))}:' +
                  k * max(s1.get(k, 0), s2.get(k, 0)) for k in dct.keys()])
    return '/'.join(sorted(lst, key=lambda st: (len(st),
                    st[0] == '1', st[0] == '2'), reverse=True))
