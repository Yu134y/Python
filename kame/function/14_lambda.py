# lambda関数（無名関数）

def square(x):
    return x * x


s = lambda x: x * x


print(square(3))
print(s(5))


def power(exponent):
    return lambda base: base ** exponent


third_power = power(3)
print(third_power(2))

numbers = [6, 2, 5, 43, 5, 36, 67, 2]

filtered_num = filter(lambda num: num % 2, numbers)
print(list(filtered_num))
