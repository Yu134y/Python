call_count = 0
CALL_COUNT = 0  # constant variable（書き換えられたくないときは大文字で定義）


def print_count1():
    global call_count
    call_count += 1
    print(f'関数1:{call_count}回目')


def print_count2():
    global call_count
    call_count += 1
    print(f'関数2:{call_count}回目')


print_count1()
print_count2()
print_count1()
print_count2()
print(call_count)