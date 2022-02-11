# Type annotation
def add_num(num1: int, num2: int) -> int:  # pythonの場合はつける必要はない
    return num1 + num2


# 動的型付け言語（python等） <-> 静的型付け言語（Java等）
one = 1
two = 2
one = 'hello'
print(add_num('1', '2'))
