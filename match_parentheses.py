def valid_parentheses(string: str) -> bool:
    if not string:
        return True
    if string[0] == ')':
        return False
    li = []
    for c in string:
        if c == '(':
            li.append(c)
        elif c == ')':
            if len(li) == 0:
                return False
            elif li[-1] == '(':
                li.pop(-1)
            else:
                return False
    return not li
