# Pythonのテスト
# 書いたコードは必ずテストする
# 昨日を開発するだけなら簡単。品質を保ちながら開発することが難しい
# テストの種類
# ・コードを実行しながら行うテスト
# ・自動で実行するテスト
# ・他モジュールや昨日との結合部分のテスト
# ・ユーザ目線での動作テスト
# ・etc...
# 単体テスト（UnitTest）と結合テスト（IntegrationTest）
# ・コンポーネント単位のテストとコンポーネント間のテスト

# assert
a = 1
b = 1
# a + b == 2
assert a + b == 2, 'a + b is equal to 2!'


def power(base, exp):
    return base ** exp


assert power(3, 2) == 9, '3 ** 2 must be 9'
