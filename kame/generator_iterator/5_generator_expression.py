# generator expression
# ・yieldを使わないでgeneratorを作る
# ・書き方はリスト内包表記と同様で、括弧を[]ではなく()を使う
# ・generator関数よりも簡潔に書ける

import sys
square_list = [num * num for num in range(100)]
print(square_list)

square_gen = (num * num for num in range(100))
print(next(square_gen))
print(next(square_gen))
print(next(square_gen))
print(next(square_gen))

print(sys.getsizeof(square_list))
print(sys.getsizeof(square_gen))

even_square = [num * num for num in range(10) if num % 2 == 0]
print(even_square)

even_square_gen = (num * num for num in range(10) if num % 2 == 0)
for num in even_square_gen:
    print(num)