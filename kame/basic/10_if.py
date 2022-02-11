# if文

age = 19
age_alcohol = 20
if age >= age_alcohol:
    print('You can drink beer!')
else:
    print('You are too young to drink beer')

age_drive = 18
if age >= age_alcohol:
    print('You can drink beer!')
elif age < age_drive:
    print('You cannot even drive!')
else:
    print('You are not allowed to drink beer but you can drive only if you have a driver\'s license')

age = -10
if not 0 < age < 120:
    print('The value is invalid')

# challenge1：もしbalance（残高）がwithdraw（引き出し額）より大きければ、balanceを更新し、そうでなければ引き出せないATMを作る
balance = 5000000
withdrawal = 1300000
if balance >= withdrawal:
    balance -= withdrawal
    print('Your new balance is {}'.format(balance))
else:
    print('You don\'t have money')

# challenge2：challenge1に加えて、引き出し額の上限を100万円に設定し、上限を超えて引き出そうとすると引き出せないATMを作る
# 自分で考えたやつ
# if withdrawal > 1000000:
#     print('The withdrawal limit is 1000000')
# elif balance >= withdrawal:
#     balance -= withdrawal
#     print(f'Your balance is {balance}')
# else:
#     print('You don\'t have money')

# 正解
withdrawal_limit = 1000000
if withdrawal > withdrawal_limit:
    print('The withdrawal limit is {}'.format(withdrawal_limit))
elif balance >= withdrawal:
    balance -= withdrawal
    print(f'Your balance is {balance}')
else:
    print('You don\'t have money')
