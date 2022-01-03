# 関数（function）

# 華氏から摂氏に変換する
fahrenheit = 72


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius


celsius = fahrenheit_to_celsius(fahrenheit)
print(celsius)
