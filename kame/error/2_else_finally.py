def split_bill(price):
    num = input('何人で割り勘しますか？')
    try:
        each = price / int(num)
    except ZeroDivisionError as e:
        print('0で割ることはできません。正しい値を入力してください')
        print(e)
    except ValueError as e:
        print('数字を入力してください')
        print(e)
    else:
        print(f'一人{each}円です')
    finally:
        print('ご利用ありがとうございます')


if __name__ == '__main__':
    split_bill(10000)

# finally:が実行されるタイミング
# ・tryでキャッチされない例外が発生した場合でもfinally:を実行してから例外を発生する
# ・except:やelse:で例外が発生しても、finally:の実行後に例外を発生する
# ・tryやbreakやcontinue、returnに達しても、その前にfinally:が実行される
# ・try:とfinally:にreturnがある場合、finally:のreturnが返される
# finallyのタイミングは複雑なので、必ず簡単なコードで試すこと
