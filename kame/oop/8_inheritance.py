# 継承（inheritance）
# オブジェクト指向の要
# ほかのクラスをベースのクラスとして継承して、別のクラスを作ることができる
# super class（親クラス、基底クラス)の昨日を引き継ぎ、sub class（子クラス、派生クラス）として拡張することができる

class Animal(object):

    def __init__(self, name):
        self.name = name
        print('Animal init is called!')

    def breath(self):
        print(f'{self.name} is breathing')


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name=name)
        print('Dog init is called')


# class Cat(Animal):
#     pass
#
#
# class Bird(Animal):
#     pass


pochi = Dog('pochi')
print(pochi.name)
pochi.breath()
