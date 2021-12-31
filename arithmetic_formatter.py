"""Arithmetic Formatter
Receives a list of strings that are arithmetic problems
and returns the problems arranged vertically and side-by-side.
The function optionally takes a second argument.
When the second argument is set to `True`, the answers should be displayed.
For example, "235 + 52" becomes:
      235
    +  52
    -----
"""

import operator


def arithmetic_arranger(lst: list[str], eval=False) -> list[str]:
    opd = {
        '+': operator.add,
        '-': operator.sub,
    }

    # problems = [[operand1, operator, operand2, spaces, ans]]
    problems = [item.split() for item in lst]

    res = []

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:

        if problem[1] in ('*', '/'):
            return "Error: Operator must be '+' or '-'."

        if not problem[0].isdigit() or not problem[2].isdigit():
            return "Error: Numbers must only contain digits."

        if len(problem[0]) > 4 or len(problem[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        problem.append(max(len(problem[0]), len(problem[2])) + 2)

        if eval:
            problem.append(
                str(opd[problem[1]](int(problem[0]), int(problem[2]))))

        operator_sign = problem.pop(1)
        spaces = problem[2]
        problem[2] = '-' * spaces
        for inx, item in enumerate(problem):
            problem[inx] = item.rjust(spaces, ' ')
        problem[1] = problem[1].replace(' ', operator_sign, 1)

    res = [''] * 4
    for i, problem in enumerate(problems):

        for inx, row in enumerate(problem):
            res[inx] += (' ' * 4 if i else '') + row

    return ('\n'.join(res) if eval else '\n'.join(res[:-1]))


print(
    repr(arithmetic_arranger(
        ['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True)))

s = '   32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028'
d = '   32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028'
