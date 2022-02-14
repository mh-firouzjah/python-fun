'''
represent numbers in given base
'''
import string


def rep_in_base(num: int, base: int = 10) -> str:
    '''
    represent `num` in base of `base`
    '''
    if base not in range(2, 37):
        raise ValueError(
            f'base: {base}',
            'base has to be between 2 and 36 inclusive')

    if num == 0:
        return '0'

    def inner(ent: int, base: int) -> tuple[int, str]:
        '''
        returns `denominator`, `reminder`
        '''
        _match = {
            **{i: i for i in range(10)},
            **
            {index + 10: char for index, char
             in enumerate(string.ascii_lowercase)}, }
        return ent // base, _match[rem] if(
            rem := ent % base) in _match.keys() else str(rem)

    denominator, reminder = inner(num, base)
    digits = [reminder]
    while denominator:
        denominator, reminder = inner(denominator, base)
        digits.insert(0, reminder)
    return ''.join(map(str, digits))


print(rep_in_base(23, 16))
print(rep_in_base(232, 36))
print(rep_in_base(10, 2))
