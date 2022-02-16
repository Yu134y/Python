# iteratorとiterable
# generatorはiteratorの一種
# iteratorとは、next()で回すことができて、iter()関数でイテレータ（iterator）を返すものの総称
# iter()関数でiteratorを返すものをiterableという
# つまりiteratorもiterableである

fruits = ['apple', 'lemon', 'peach']

# print(next(fruits))
fruits_iterator = iter(fruits)
print(next(fruits_iterator))
print(id(fruits_iterator))
print(id(iter(fruits_iterator)))

print('=' * 30)
print(next(fruits_iterator))
print(fruits_iterator.__next__())

# next()と.__next__()
# ・next(obj)はobj.__next__()と等しい
# ・__xxx__はmagic methodと呼ばれる特別なメソッド
# ・他のmagic methods:__init__, __len__, __str__, __doc__, ...
# ・next()で値を返すということは、__next__メソッドを実装しているということ
# ・同様に、iter()は__iter__()メソッドをcallしている
# ・つまり、iteratorは__next__()と__iter__()が正しく実装されたオブジェクト
