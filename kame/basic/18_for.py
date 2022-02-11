# forループ

fruits = ['apple', 'peach', 'grapes', 'banana']

for fruit in fruits:
    print(f'I love {fruit}!!')

for char in 'hello world!!':
    print(f'char: {char}')

# ループで回すことをiterationという。iterationできるものをiterableという。

# challenge1：ユーザに好きなフルーツを入力してもらい、fruitsリストの各フルーツに対して「好き/好きじゃない」をprint()する
# 自分で考えたやつ(正解と一緒）
favorite_fruits = input('好きなフルーツはなんですか？')

for fruit in fruits:
    if favorite_fruits == fruit:
        print('{}は好き'.format(fruit))
    else:
        print('{}は好きじゃない'.format(fruit))

# challenge2：fruitsリストの各フルーツに対して「好き/好きじゃない」をユーザに聞いて、好きなフルーツリスト、好きじゃないフルーツリストを作成する
# 自分で考えたやつ（全ての要素を入れたリストを作成できなかった、リストは外に作る）
for fruit in fruits:
    fruits_list = input('{}は好きですか？ y/n'.format(fruit))
    if fruits_list == 'y':
        yes_fruits = []
        yes_fruits.append(fruit)
    else:
        no_fruits = []
        no_fruits.append(fruit)

print('好きなフルーツリスト：', yes_fruits)
print('嫌いなフルーツリスト：', no_fruits)

# 正解
favorite_fruits = []
normal_fruits = []
for fruit in fruits:
    choice = input(f'{fruit}は好き？ y/n')
    if choice == 'y':
        favorite_fruits.append(fruit)
    else:
        normal_fruits.append(fruit)

print(f'favorite fruits: {favorite_fruits}')
print(f'normal fruits: {normal_fruits}')
