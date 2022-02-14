# raise
# ・特定の例外を発生させることができる
# ・raise<例外クラス>もしくはraise<例外インスタンス>の形をとる(raise ValueError/raise ValueError())
# ・例えばtry exceptをテストする際に使う

try:
    # TODO あとで削除する
    raise ValueError()
except ValueError:
    print('Do something')
    raise
