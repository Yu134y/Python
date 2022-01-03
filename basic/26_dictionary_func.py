fruits_color = {'apple': 'red', 'lemon': 'yellow', 'grapes': 'purple'}
# print(fruits_color['peach'])  # dictionaryにないとエラーになる

if 'peach' in fruits_color:
    print(fruits_color['peach'])
else:
    print('the key is not found')

# .get() keyがない可能性があるなら使う
fruit = input('フルーツの名前を指定してください')
print(fruits_color.get(fruit, 'Nothing'))

# .update() dictionary同士の結合
fruits_color2 = {'peach': 'pink', 'kiwi': 'green'}
fruits_color.update(fruits_color2)
print(fruits_color)