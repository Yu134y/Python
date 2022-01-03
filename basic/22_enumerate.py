# enumerate()：indexとリストの要素を返す
fruits = ['apple', 'peach', 'grapes', 'banana']

for idx, fruit in enumerate(fruits):
    print(idx)
    print(fruit)

for x in enumerate(fruits):
    print(x)