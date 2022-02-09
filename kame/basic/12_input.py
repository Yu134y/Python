# input()：ユーザの入力した値（文字列）を取得する

age = input('何歳ですか？')  # inputで代入された数字は文字列扱い
print('あなたは{}歳です'.format((age)))


# challenge1：ユーザに年齢を聞き、18歳以上なら入れるカジノを作成する
# 自分で考えたやつ
age = input('何歳ですか？')

if int(age) >= 18:  # ハードコーディングは扱わない！
    print('どうぞお入りください')
else:
    print('18歳未満の方はカジノへは入れません')

# 正解
age = int(input('何歳ですか？'))
casino_age = 18

if age >= casino_age:
    print('どうぞお入りください')
else:
    print('{}歳未満の方はカジノへは入れません'.format(casino_age))

# challenge2：カジノに入ったらゲームを選べるようにする。
# 選択できるゲームは1．ルーレット、2．ブラックジャック、3．ポーカー、選択後、ゲーム内容をprint()する
# 自分で考えたやつ
game = int(input('ゲームを選択してください：1．ルーレット、2．ブラックジャック、3．ポーカー'))

if game == 1:
    print('ルーレットとは、、、')
elif game == 2:
    print('ブラックジャックとは、、、')
else:
    print('ポーカーとは、、、')

# 正解
age = int(input('何歳ですか？'))
casino_age = 18
game_text = '''プレイするゲームを選択してください
1：ルーレット
2：ブラックジャック
3：ポーカー
'''

if age >= casino_age:
    print('どうぞお入りください')
    game = input(game_text)
    if game == '1':
        print('あなたはルーレットを選びました')
    elif game == '2':
        print('あなたはブラックジャックを選びました')
    elif game == '3':
        print('あなたはポーカーを選びました')
    else:
        print('1~3を選んでください')
else:
    print('{}歳未満の方はカジノへは入れません')
