# __init__.pyを置くことで、Pythonはそのディレクトリをパッケージとして認識する
# __init__.pyには初期化用コードを記述する（import時に実行される)
# __init__.pyにimport文を書くことでモジュール名をスキップしてpackage.の後に関数名やクラス名にアクセスできる
# __init__.pyに__all__を定義することで、そのパッケージがimport*でインポートされた際にインポートさせる関数やクラスを定義することができる

from myfirstpackage.subdir.module2 import *