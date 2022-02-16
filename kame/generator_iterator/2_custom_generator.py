# range(10)
def my_range(stop):
    start = 0
    while start < stop:
        yield start
        start += 1


# yield
# returnの代わりにyieldを使うと、その関数はgenerator(generator function)になる
# generator functionの戻り値はgenerator iteratorと呼ばれるもので、イテレーションによりyieldの値を返すオブジェクトになる

# mr = my_range(10)
# print(type(mr))  # generator
# print(next(mr))  # 0
# print(next(mr))  # 1
# print(next(mr))  # 2
# print(next(mr))  # 3
# print(next(mr))  # 4
# print('end of next()')
# print(next(mr))  # 5
# print(next(mr))  # 6
# print(next(mr))  # 7
# print(next(mr))  # 8
# print(next(mr))  # 9
# print(next(mr))

# print('beginning of for loop')
# for i in my_range(10):
#     print(i)


# challenge：指定した数字から2までの偶数の値を返すgeneratorを作ろう
# 自分で考えたやつ
def return_even(start):
    stop = 2
    while stop <= start:
        if start % 2 == 0:
            yield start
            start -= 2
        else:
            start -= 1


for i in return_even(15):
    print(i)


# 正解
def even(num):
    while num != 0:
        if num % 2 == 0:
            yield num
        num -= 1


for i in even(10):
    print(i)

even_gen = even(10)
print(next(even_gen))
print(next(even_gen))
print(id(even_gen))
print(id(iter(even_gen)))
