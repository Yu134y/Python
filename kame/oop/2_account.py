# challenge：銀行のAccountクラスを作ろう
# 残高（balance）と口座名（name）をもとに口座（Account）を作る
# withdrawメソッドとdepositメソッドで残高を変更する
# 残高が足りなければ引き落とせないようにする
# 口座番号（account_number）はいままで作成された口座のIDとなるように連番を振る（0, 1, 2, 3, 4, ...）
# 残高が変更されたら口座名、口座番号とその残高を表示する

# 自分で考えたやつ

# class Account(object):
#
#     account_number = 0
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         Account.account_number += 1
#
#     def withdraw(self):
#         while True:
#             withdraw_money = int(input('引き出し金額を入力してください：'))
#             if self.balance >= withdraw_money:
#                 self.balance -= withdraw_money
#                 self.show_balance()
#                 break
#             else:
#                 print(f'残高が不足しています（残高：{self.balance}）')
#
#     def deposit(self):
#         deposit_money = int(input('お預け金額を入力してください：'))
#         self.balance += deposit_money
#         print(self.balance)
#         self.show_balance()
#
#     def show_balance(self):
#         print(f'ご利用ありがとうございます。\n口座名：{self.name} \n口座番号：{Account.account_number} \n残高：{self.balance}円')
#
#
# john = Account('John', 50000)
# print(john.name)
# print(john.balance)
# print(Account.account_number)
#
# john.withdraw()
# john.deposit()
#
# yu = Account('Yu', 100000)
# print(yu.name)
# print(yu.balance)
# print(Account.account_number)
#
# yu.withdraw()
# yu.deposit()


# 正解
class Account:
    count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = Account.count
        self.show_balance()
        Account.count += 1

    def withdraw(self, price):
        if price <= self.balance:
            self.balance -= price
            self.show_balance()
        else:
            print(f'残高（{self.balance}円）が足りません')

    def deposit(self, price):
        self.balance += price
        self.show_balance()

    def show_balance(self):
        # print(f'{self,name}の残高は{self.balance}円です')
        print('{0.name}（口座番号：{0.account_number})の残高は{0.balance}円です'.format(self))


my_account = Account(name='my account', balance=1000)
print(my_account.name)
print(my_account.balance)
my_account.withdraw(300)
my_account.deposit(500)
my_account.withdraw(1500)
your_account = Account(name='your account', balance=10000)
your_account.deposit(5000)
