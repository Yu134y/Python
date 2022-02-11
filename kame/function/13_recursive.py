# 再帰関数（recursive function）：関数内で自身の関数をcallする関数
# 階乗（factorial）：3! = 3 × 2 × 1 = 6
# n! = n * (n-1) * (n-2) * ... * 1
# n! = n * (n-1)!

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(3))


# challenge1：Fibonacci数を計算する関数を再帰で実装してみよう。
# フィボナッチ数列：(0), 1, 1, 2, 3, 5, 8, ...
# 例：fibonacci(6) = 8
def fibonacci_recursive(n):
    if n < 2:
        return n
    else:
        return fibonacci_recursive(n-2) + fibonacci_recursive(n-1)


print(fibonacci_recursive(5))


# challenge2：Fibonacci数を計算する関数を再帰なしで実装して、再帰と比べてどちらが早いか確認してみよう
def fibonacci(n):
    if n < 2:
        return n
    else:
        n_1 = 1
        n_2 = 0
        for _ in range(n-1):
            result = n_2 + n_1
            n_2 = n_1
            n_1 = result
        return result


print(fibonacci(3))

for i in range(50):
    print(i, fibonacci(i))
