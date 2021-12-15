# def move_zeros(array):
#     zeros = sorted(array)
#     i = 0
#     while i < len(zeros):
#         if zeros[i] == 0:
#             i += 1
#             continue
#         zeros = zeros[:i]
#         break
#     i = 0
#     while i < len(array):
#         if array[i] == 0:
#             array.pop(i)
#             i -= 1
#         i += 1
#     return array + zeros

def move_zeros(array):
    return sorted(array, key=lambda x: x == 0)


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
# returns [1, 1, 2, 1, 3, 0, 0]
