class MyIterator:
    def __init__(self, start=0):
        self.current = start

    def __next__(self):
        num = self.current
        self.current += 1
        return num

    def __iter__(self):
        return self


# myiterator = MyIterator(10)
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(id(myiterator))
# print(id(iter(myiterator)))


# challenge：指定した数字から2までの偶数の値を返すiteratorを作ってみよう（generator関数を使わずに）
# 自分で考えたやつ
# class EvenIterator:
#     def __init__(self, start=0):
#         self.current = start
#
#     def __next__(self):
#         num = self.current
#         while num != 0:
#             if num % 2 == 0:
#                 return self.current
#             num -= 1
#
#     def __iter__(self):
#         return self
#
#
# for i in EvenIterator(10):
#     print(i)


# 正解
class EvenIterator:
    def __init__(self, start):
        self.current = start

    def __next__(self):
        if self.current < 2:
            raise StopIteration
        elif self.current % 2 == 0:
            num = self.current
            self.current -= 2
            return num
        else:
            self.current -= 1
            return self.__next__()

    def __iter__(self):
        return self

if __name__ == '__main__':
    even = EvenIterator(10)
    print(next(even))
    print(next(even))
    print(next(even))
    print(next(even))
    print(next(even))
    print(next(even))

