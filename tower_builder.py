def tower_builder(n_floors: int) -> list[str]:
    return [('*' * (2 * i - 1)).center(2 * n_floors - 1, ' ')
            for i in range(1, n_floors + 1)]


print(tower_builder(1))
print(tower_builder(2))
print(tower_builder(3))

# ['*']
# [' * ', '***']
# ['  *  ', ' *** ', '*****']
