# private変数と名前修飾（name mangling）
# private変数は、クラス外からアクセスできない変数
# Pythonには「private変数」はない
# 外からアクセスされないと想定している変数には_をつける（習慣であってpythonによる強制力はない）<- nonpublic
# 「__」（2つのアンダースコア）をつけることで名前修飾する
# 名前修飾された変数名は_<Class>__<attribute>（例：_Account__balance）のような形になる
# 結果、private変数のような役割をつけることができる(private変数ではない)


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


my_account = Account(10000)
print(dir(my_account))
my_account.deposit(2000)
my_account.withdraw(5000)
my_account.withdraw(10000)
print(dir(my_account))
my_account.__balance = -10000  # 直接更新しても名前修飾された__balanceに影響はなく、また新たに__balanceが作られる
print(my_account.__balance)  # -10000
my_account.show_balance()  # 7000
print(dir(my_account))
my_account._Account__balance = -10000  # 名前修飾され__balanceを指定すると更新されるので、アクセスすることができないわけではない
