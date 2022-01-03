# in演算子

fruits = ['apple', 'peach', 'grapes', 'banana']
print('apple' in fruits)  # True
print('lemon' in fruits)  # False
print('lemon' not in fruits)  # True
print('h' in 'hello')  # True

# challenge：ユーザに好きなフルーツを入力してもらい、そのフルーツがfruitsリストにあればそのフルーツを削除し、なければそのフルーツを追加するプログラムを作る
# 自分で考えたやつ
favorite_fruits = input('好きなフルーツを入力してください')

if favorite_fruits in fruits:
    fruits.remove(favorite_fruits)
    print(fruits)
elif favorite_fruits not in fruits:
    fruits.append(favorite_fruits)
    print(fruits)
else:
    print('フルーツを入力してください')

# 正解
favorite = input('好きなフルーツはなんですか？')

if favorite in fruits:
    print('{}ですね。差し上げますよ'.format(favorite))
    fruits.remove(favorite)
else:
    print('{}ですね。仕入れました！'.format(favorite))
    fruits.append(favorite)

print('今あるフルーツはこちらです。{}'.format(fruits))