# 例外(Exception)
# ・例外が起きると、プログラムはクラッシュする
# ・例外が起きる可能性がある場合は、例外を処理(exception handling)する必要がある
# ・Pythonにはすでに色々な例外がクラスとして定義されている(https://docs.python.org/3/library/exceptions.html)

def split_bill(price):
    num = input('何人で割り勘しますか？')
    try:
        each = price / int(num)
    except ZeroDivisionError as e:
        print('0で割ることはできません。正しい値を入力してください')
        each = price
        print(e)
    except ValueError as e:
        print('数字を入力してください')
        each = price
        print(e)
    print(f'一人{each}円です')


if __name__ == '__main__':
    split_bill(10000)
