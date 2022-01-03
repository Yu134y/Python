# range(10)
def myrange(stop):
    start = 0
    while start < stop:
        yield start
        start += 1

# yield
# returnの代わりにyieldを使うと、その関数はgenerator(generator function)になる
# generator functionの戻り値はgenerator iteratorと呼ばれるもので、イテレーションによりyieldの値を返すオブジェクトになる

# mr = myrange(10)
# print(type(mr))
# print(next(mr))
# print(next(mr))
# print(next(mr))
# print(next(mr))
# print(next(mr))
# print('end of next()')
# print(next(mr))
# print(next(mr))
# print(next(mr))
# print(next(mr))
# print(next(mr))  # 9
# print(next(mr))

# print('beginning of for loop')
# for i in myrange(10):
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