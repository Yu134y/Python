# 「：」を使って、複数の要素をとってくることができる（slicing)

even = [2, 4, 6, 8, 10, 12]
# 基本は[開始:未満]
print(even[1:4])  # ○以上○未満をとってくる
print(even[0:4])
print(even[:4])  # 0は省略可能

print(even[3:5])
print(even[3:-1])  # indexに負の値を指定することも可能

print(even[3:])

print(even[:])  # 全ての要素をとってくる

text = 'hello world'
print(text[3:])

# [開始:未満:step]
print(text[2:10:2])

print(text[::-1])  # 逆順