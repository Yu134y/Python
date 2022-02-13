# ポリモーフィズム（polymorphism）
# polyはmany, morpheはform　つまり多態性という意味
# intもstrもprint()とすることでprintすることができる
# print_int()やprint_str()などのように型にあった関数を呼ぶ必要がない
# 継承はポリモーフィズムを実現する手段の1つ


class MyClass:
    def __str__(self):
        return 'MyClassの__str__'


mc = MyClass()
print(mc)  # mc.__str__()
print(1)  # 1.__str__()
print('1')  # '1'.__str__()
print(True)  # True.__str__()
print([1, 2, 3])  # [1, 2, 3].__str__()


def print_value(arg):
    print(arg + 1)


print_value(True)

various_types = [1, '1', True, [1, 2, 3], (1,), {'1': 1}, {1}]
# for elem in various_types:
#     print(elem)
