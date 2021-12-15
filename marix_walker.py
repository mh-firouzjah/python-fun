def move_top(pos: tuple, matrix: list) -> tuple:
    if pos[0] - 1 >= 0 and matrix[pos[0] - 1][pos[1]] != '0':
        return (pos[0] - 1, pos[1])


def move_right(pos: tuple, matrix: list) -> tuple:
    max_col = len(matrix[0])
    if pos[1] + 1 < max_col and matrix[pos[0]][pos[1] + 1] != '0':
        return (pos[0], pos[1] + 1)

def matrix_walker(matrix: list, cp, start, end, count) -> list:
    if cp == end:
        return [cp]
    if cp:
        top = None
        right = None
        mt = move_top(cp, matrix)
        mr = move_right(cp, matrix)
        mw1 = matrix_walker(matrix, mt, start, end, count)
        mw2 = matrix_walker(matrix, mr, start, end, count)
        if mt and mw1:
            if mt != end:
                top = [mt, *mw1]
            else:
                top = [mt, end]
                count[-1] += 1

        if mr and mw2:
            if mr != end:
                right = [mr, *mw2]
            else:
                right = [mr]
                count[-1] += 1
        if top and right:
            return [top, right]
        if top or right:
            return top or right


matrix = [
    ['1', '1', '1', '1'],
    ['1', '1', '1', '0'],
    ['1', '0', '1', '1'],
    ['1', '1', '1', '1']
]

start = (len(matrix) - 1, 0)
end = (0, len(matrix[0]) - 1)
cp = start
count = [0]
ans = matrix_walker(matrix, cp, start, end, count)

# ['1', '1', '1', '1'],
# ['1', '1', '1', '0'],
# ['1', '0', '1', '1'],
# ['1', '1', '1', '1']
# [
#     [(2, 0), (1, 0),
#                   [(0, 0), (0, 1), (0, 2), (0, 3)],
#                   [(1, 1),
#                       [(0, 1), (0, 2), (0, 3)],
#                       [(1, 2), (0, 2), (0, 3)]
#                   ]
#     ],
#     [(3, 1), (3, 2), (2, 2), (1, 2), (0, 2), (0, 3)]
# ]

print(ans)
