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