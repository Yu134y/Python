# スタティックメソッド（static method）
# インスタンスに紐づかないメソッド
# @staticmethodデコレータを使う
# 主にクラス内で便利関数のように使用する
# 引数にselfを取らない（インスタンスの情報は使わないので）
# クラスからアクセスしてcallする（<class>.<staticmethod>()）
# クラスの情報を使う場合はクラスメソッドを使う
import time


class MyClass:

    def mymethod(self):
        print('This is normal method! from {}'.format(self))

    @staticmethod
    def mystaticmethod():
        print('This is staticmethod!')


c = MyClass()
c.mymethod()
MyClass.mystaticmethod()
# c.mystaticmethod()  # こういう形で呼ぶ必要はない


# challenge：前回のchallengeで作成したAccountクラスに、取引（transaction）を記録する仕組みを追加する
# 取引（transaction）として保持する情報は、・'withdraw/depositの金額'　・'新しい残高'　・'日時'
# それぞれの取引情報をdictionaryとして保持し、それをlistでインスタンス変数で保持すればOK
# '日時'を作る関数をstaticmethodで作ってみよう

class Account:

    count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = Account.count
        self.transaction_history = []
        Account.count += 1

    def withdraw(self, price):
        if price <= self.balance:
            self.balance -= price
            self.show_balance()
            self.add_transaction(-price)
        else:
            print(f'残高（{self.balance}円）が足りません')

    def deposit(self, price):
        self.balance += price
        self.show_balance()
        self.add_transaction(price)

    def show_balance(self):
        # print(f'{self,name}の残高は{self.balance}円です')
        print('{0.name}（口座番号：{0.account_number})の残高は{0.balance}円です'.format(self))

    def add_transaction(self, price):
        transaction = {
            'withdraw/deposit': price,
            'new_balance': self.balance,
            'time': Account.get_time_str()
        }
        self.transaction_history.append(transaction)

    @staticmethod
    def get_time_str():
        current_time = time.localtime()
        return '{0.tm_year}年{0.tm_mon}月{0.tm_mday}月{0.tm_hour}時{0.tm_min}分'.format(current_time)

    def show_transaction_history(self):
        for transaction in self.transaction_history:
            transaction_str_list = []
            for k, v in transaction.items():
                transaction_str_list.append(f'{k}: {v}')
            print(', '.join(transaction_str_list))


myaccount = Account(name='my account', balance=1000)
print(myaccount.balance)
myaccount.withdraw(300)
myaccount.deposit(500)
myaccount.withdraw(1500)
print(myaccount.transaction_history)
myaccount.show_transaction_history()