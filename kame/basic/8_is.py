# is演算子：同じオブジェクトかどうかを判定する

a = 1
b = 1
c = 3
d = a
e = 2 - 1  # 1

print(id(a))
print(id(b))
print(id(1))

print(a is b)  # True
print(a is not c)  # True

print(d is a)  # True
print(d is b)  # True

print(a is e)  # True

hello = 'hello'
hello2 = 'h' + 'e' + 'l' + 'l' + 'o'  # hello
print(hello, hello2)
print(hello is hello2)  # True
hello = 'konnichiwa'
print(hello is hello2)  # False


# Noneかどうかの判定によく使う
nothing = None
print(nothing is None)  # True
print(id(nothing))
print(id(None))
