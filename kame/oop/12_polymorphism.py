# ポリモーフィズム（polymorphism）
# polyはmany, morpheはform　つまり多態性という意味
# intもstrもprint()とすることでprintすることができる
# print_int()やprint_str()などのように型にあった関数を呼ぶ必要がない
# 継承はポリモーフィズムを実現する手段の1つ


class MyClass:
    def __str__(self):
        return 'MyClassの__str__'


def printvalue(arg):
    print(arg + 1)


printvalue(True)

various_types = [1, '1', True, [1, 2, 3], (1,), {'1': 1}, {1}]
# for elem in various_types:
#     print(elem)