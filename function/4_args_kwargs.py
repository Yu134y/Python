# *args（不特定多数の引数を渡すことが可能、tupleで受け取る）
def get_average(*args):
    num = len(args)
    if num == 0:
        return 0
    total = sum(args)
    return total / num


average = get_average(1, 2, 3, 4, 5, 6, 7, 8)
print(average)

# **kwargs（dictionaryで受け取る）
def kwargs_func(**kwargs):
    param1 = kwargs.get('param1', 1)
    param2 = kwargs.get('param2', 2)
    param3 = kwargs.get('param3', 3)

    print(f'param1: {param1}, param2: {param2}, param3: {param3}')


kwargs_func(param1=10, param2=6, param3=100, param4=4)

# *と**はunpacking operator
numbers = (1, 2, 3)
print(*numbers)
print(1, 2, 3)

a = {'a': 1, 'b': 2}
b = {'c': 3, 'd': 4}
c = {**a, **b}
print(c)