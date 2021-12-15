import re


def is_interesting(number, awesome_phrases):
    def followed_by_zeros(string):
        return bool(re.match(r'^0+$', string[1:])) or False

    def digit_is_same_number(string):
        return bool(re.match(fr'^{string[0]}+$', string[1:])) or False

    def is_sequential(string):
        if len(string) < 2:
            return False

        def is_seq(t):
            a, b = t[0], t[1]
            if int(a) == int(b) + 1:
                return True
            return False

        if string[:2] == '01':
            if string[-2:] == '90':
                return False
            return all(is_seq(item) for item in zip(string[1:], string[:-1]))
        if string[-2:] == '90':
            return all(is_seq(item[::-1])
                       for item in zip(string[1:], string[:-1]))
        return all(is_seq(item) for item in zip(string[1:], string[:-1])) or all(
            is_seq(item[::-1]) for item in zip(string[1:], string[:-1]))

    def is_palindrome(string):
        if len(string) < 2:
            return False
        return string == string[::-1]

    def is_in_awesome_phrases(number):
        return number in awesome_phrases
    s1 = str(number)
    r1 = max(is_in_awesome_phrases(number), is_palindrome(s1),
             is_sequential(s1), digit_is_same_number(s1),
             followed_by_zeros(s1))
    if r1:
        return 2
    s2 = str(number + 1)
    r2 = max(is_in_awesome_phrases(number + 1), is_palindrome(s2),
             is_sequential(s2), digit_is_same_number(s2),
             followed_by_zeros(s2))
    s3 = str(number + 2)
    r3 = max(is_in_awesome_phrases(number + 2), is_palindrome(s3),
             is_sequential(s3), digit_is_same_number(s3),
             followed_by_zeros(s3))
    return int(r2 or r3)


tests = [
    # {'n': 3, 'interesting': [1337, 256], 'expected': 0},
    # {'n': 1336, 'interesting': [1337, 256], 'expected': 1},
    # {'n': 1337, 'interesting': [1337, 256], 'expected': 2},
    # {'n': 11208, 'interesting': [1337, 256], 'expected': 0},
    # {'n': 11209, 'interesting': [1337, 256], 'expected': 1},
    # {'n': 11211, 'interesting': [1337, 256], 'expected': 2},
    {'n': 97, 'interesting': [], 'expected': 0},
    {'n': 88, 'interesting': [], 'expected': 0},
    {'n': 30, 'interesting': [], 'expected': 0},
]
for t in tests:
    print(is_interesting(t['n'], t['interesting']), t['expected'])
