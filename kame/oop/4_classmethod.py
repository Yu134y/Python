# クラスメソッド
# インスタンスに紐づかないメソッド
# @classmethodデコレータを使う
# 主にクラス内で便利関数のように使用する
# 引数にclsを取ってクラスの情報にアクセスできる
# クラスからアクセスしてcallする（<Class>.<classmethod>）
# クラスの情報を使わない場合はスタティックメソッドを使う
# クラスメソッド内でインスタンスを生成して返すことも可能

class MyClass:

    classmethod_count = 0

    def mymethod(self):
        print('This is normal method! from {}'.format(self))

    @staticmethod
    def mystaticmethod():
        print('This is staticmethod!')

    @classmethod
    def myclassmethod(cls):
        cls.classmethod_count += 1
        print(f'This is classmethod and now the count is {cls.classmethod_count}')

c = MyClass()
c.mymethod()
MyClass.mystaticmethod()
MyClass.myclassmethod()
c.myclassmethod()