# "+"演算子でリストを結合する

print([1, 2, 3] + [4, 5, 6])

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(a + b)
print(c)

# a.append(b)  # append()とごちゃごちゃにならないように
print(a)

a += b
print(a)
