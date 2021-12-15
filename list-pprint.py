'''custom list printing function'''


def func(list_: list[list[str]]) -> None:
    '''takes a list and pretty prints it'''
    largest = max([max([len(it) for it in li])for li in list_])
    ljust = largest + 1
    liner = '#' * (len(list_[0]) * ljust + len(list_[0])*2 + 1)
    print(liner)
    for row in list_:
        for col in row:
            print('# '+col.ljust(ljust), end='')
        print('#')
        print(liner)


func([['1', '23', '456'],
      ['7', '89', '1234']])
