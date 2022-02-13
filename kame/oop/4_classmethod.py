# クラスメソッド
# インスタンスに紐づかないメソッド
# @classmethodデコレータを使う
# 主にクラス内で便利関数のように使用する
# 引数にclsを取ってクラスの情報にアクセスできる
# クラスからアクセスしてcallする（<Class>.<classmethod>）
# クラスの情報を使わない場合はスタティックメソッドを使う
# クラスメソッド内でインスタンスを生成して返すことも可能

class MyClass:
    class_method_count = 0

    def my_method(self):
        print('This is normal method! from {}'.format(self))

    @staticmethod
    def my_static_method():
        print('This is staticmethod!')

    @classmethod
    def my_class_method(cls):
        cls.class_method_count += 1
        print(f'This is classmethod and now the count is {cls.class_method_count}')


c = MyClass()
c.my_method()
MyClass.my_static_method()
MyClass.my_class_method()
c.my_class_method()
