# 関数の中で関数を定義（nested function）
msg = 'I am global'


def outer():
    msg = 'I am outer'

    def inner():
        nonlocal msg  # 外側の関数にアクセスできる
        msg = 'I am inner'
        print('This is inner function')
        print(msg)
    inner()
    print(msg)


outer()
print(msg)
