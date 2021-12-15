"""Given an input string of:
```py
apples, pears # and bananas
grapes
bananas !apples```

The output expected would be:
```py
apples, pears
grapes
bananas```

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""


def solution(string, markers):
    strings = string.split('\n')
    for marker in markers:
        for inx, sub_string in enumerate(strings):
            if marker in sub_string:
                strings[inx] = sub_string[:sub_string.index(marker)].strip()
    return '\n'.join(strings)


print(
    solution(
        "apples, pears # and bananas\ngrapes\nbananas !apples", [
            "#", "!"]))
print(solution("a #b\nc\nd $e f g", ["#", "$"]))
