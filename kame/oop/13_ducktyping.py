# ダックタイピング
# 動的型付け言語における考え方
# "If if walks like a duck and quacks like a duck, it must be a duck"
# Python的にいうと「オブジェクトのクラス（型）には興味がなく、振る舞いに興味がある」ということ
# 「アヒルかどうか」よりも「アヒルのように歩くか、鳴くか」に興味がある
# 「intかどうか」よりも「+の演算ができるかどうか」に興味があり、「+の演算ができるならintとして扱ってもいいよね」ということ


class Duck:
    """
    This is a class for Duck

    Attributes:
        name (str): the name of the duck

    Methods:
        walk: print ***
        quack: print ***
        fly: print ***
    """

    def __init__(self, name):
        """
        The constructor for Duck class
        :param name: the name of the duck
        """
        self.name = name

    def walk(self):
        print('walking...')

    def quack(self):
        print('quack quack...!')

    def fly(self):
        print('Whee!!')


class Penguin:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print('walking...')

    def quack(self):
        print('quack quack...??')

    def swim(self):
        print('Swimming!')


def walk_and_quack(duck):
    print(f'I\'m {duck.name}')
    duck.walk()
    duck.quack()


if __name__ == '__main__':
    print(help(Duck))
    print(Duck.__doc__)
    donald = Duck('Donald')
    scrooge = Duck('Scrooge')
    daisy = Duck('Daisy')
    pingu = Duck('Pingu')
    duck_list = [donald, scrooge, daisy, pingu]
    for duck in duck_list:
        walk_and_quack(duck)
