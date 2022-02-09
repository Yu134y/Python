# 変数へ代入：assignment

# 変数の名前を変える場合はRefactor→Renameで変えると同じ名前の変数を一度に変えられるので便利
hello = 'Hello'
world = 'World!!'
print(hello + world)
print('Hello' + 'World!!')  # ハードコーディングはなるべく避ける

# 変数の命名規則(naming convention)
#   - snake_case(pythonではsnake_case)
#   - 文字から始まる
#   - 文字、数字、_（アンダースコア）を使う
#   - Case sensitive(Helloとhelloは別の変数、大文字と小文字は区別)


# format（現在の主流）
print('hello {}'.format('world'))  # formatは{}の中に値を入れることができる
print('{} {}'.format(hello, world))

name = 'Yu'
print('Hey, {}!! How are you doing?'.format(name))

balance = 100
print('balance: {}'.format(balance))

# fstring（formatの別のやり方、今後推奨）
print(f'{hello} {world}')  # {}の中に直接変数、関数を書ける、クオーテーションの前にfをつける
print(f'Hey, {name}!! How are you doing?')
print(f'balance: {balance}')
