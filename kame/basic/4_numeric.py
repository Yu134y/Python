# 数値型(Numeric): integer, float, complex

# int(integer, 整数) -3, -2, -1, 0, 1, 2, 3, 100
print(type(1))

# float(浮動小数点)
# 0.1などの少数は足し算などで積み重なると誤差が生じる
print(type(0.1))
print(0.1 + 0.1 + 0.1)  # 0.3


# Numeric Operator(数値演算子)

# 四則演算
print(1 + 0.4)
print(1 - 0.4)
print(2 * 3)
print(1 / 2)
print(5 * 6 - 3 / 6)

result = 1 + 1.0
print(result)
print(type(result))
print(f'type of result: {result} is {type(result)}')

# その他の演算子
# floor division
print(14 // 4)  # 割り算の整数部分を抽出
# modulo
print(14 % 3)  # 割り算のあまりの値を抽出
# exponentiation
print(2 ** 3)  # べき乗

hit_point = 100
attack_point = 40.3
remain = hit_point - attack_point
print(f'remain hit point is {remain}')

# augmented assignment +=, -=, *=, /=
a = 1
a = a + 1
a += 1  # a = a + 1と同じ
print(a)
