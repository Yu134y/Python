# private変数と名前修飾（name mangling）
# private変数は、クラス外からアクセスできない変数
# Pythonには「private変数」はない
# 外からアクセスされないと想定している変数には_をつける（習慣であってpythonによる強制力はない）<- nonpublic
# 「__」（2つのアンダースコア）をつけることで名前修飾する
# 名前修飾された変数名は_<Class>__<attribute>（例：_Account__balance）のような形になる
# 結果、private変数のような役割をつけることができる


class Account:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        self.show_balance()

    def withdraw(self, amount):
        if self.__balance < amount:
            print('残高が足りません')
        else:
            self.__balance -= amount
            self.show_balance()

    def show_balance(self):
        print(f'残高は{self.__balance}円です')


myaccount = Account(10000)
print(dir(myaccount))
myaccount.deposit(2000)
myaccount.withdraw(5000)
myaccount.withdraw(10000)
print(dir(myaccount))
myaccount.__balance = -10000
print(myaccount.__balance)
myaccount.show_balance()
print(dir(myaccount))