# range(start, stop, step)

for i in range(1, 7):
    print(i)

for i in range(4, 13, 2):
    print(i)

for i in range(10):
    print(i)

for _ in range(10):  # _はこの変数を何も使わないときに使う
    print('hello')

# challenge：FizzBuzzゲームを作ろう！
# 1～50の数字をそれぞれprint()して、3の倍数で「Fizz」、5の倍数で「Buzz」、3と5の倍数で「FizzBuzz」とprint()する
# 自分で考えたやつ（正解と一緒）
for i in range(1, 51):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
