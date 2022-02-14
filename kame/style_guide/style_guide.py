# 変数の定義
# correct
import math

x = 1
y = 1

# wrong
x       = 1
y       = 1
x = 1


# 関数の引数の「=」にはスペースは不要
# correct
def complex(real, imag=0.0):
    return magic(r=real, i=imag)

# wrong
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)


# operatorの周りにスペース一個,operatorにpriorityがある場合はスペースをなくす
# correct
x = x + 1
x += 1
x = x*2 - 1
a = x*x + y*y
c = (a+1) * (a-1)

# wrong
x=x+1
X +=1
x = x * 2 - 1
a = x * x + y *y
c = (a + 1) * (a -1)


# カンマの後にはスペースを入れる
# correct
range(1, 11)
a = [1, 2, 3, 4]
b = (1, 2, 3, 4)

# wrong
range(1,11)
a = [1,2,3,4]
b = (1,2,3,4)


# カンマの後に閉じかっこがくる場合はスペースは不要
# correct
foo = (0,)

# wrong
foo (0, )

# correct
FILES = [
    'setup.cfg',
    'tox.ini',
]

# wrong
FILES = ['setup.cfg', 'tox.ini',]


# 行の折り返し
# correct
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

# wrong
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# correct
def long_function_came(
        var_one, var_two, var_three, var_four):
    print(var_one)

# wrong
def long_function_came(
    var_one, var_two, var_three, var_four):
    print(var_one)


# '\'で区切って改行する
print('このように表示する文章が違ったり長かったりする場合は\
バックスラッシュで区切ると改行できます')

# correct
a = 100000000000000000000000 \
    + 100000000000000000 \
    + 100000000 \
    + 10000000000

# wrong
a = 100000000000000000000000 +\
    100000000000000000 +\
    100000000 +\
    10000000000


# 関数間は二行開ける
def func():
    pass


def func2():
    pass


# クラス内のメソッド間は一行開ける
class MyClass:
    def __init__(self):
        pass

    def method(self):
        pass


# importのStyle
# correct
import os
import sys

# wrong
import os, sys

# correct
from subprocess import Popen, PIPE

# 順番
# 1．Standard library(time, sys)
# 2. Third party(numpy, pandas)
# 3. our library
# 4. Local library
# それぞれ一行開ける(abc順)

# absolute import
import mypkg.sibling
from mypkg import sibling
from myokg.sibling import example

from package.subpackage1.subpackage2.subpackage3.module4 import function


# コメント
# ・コメントは常に最新にする。コメントとコードの中身が異なるなら、コメントはない方がまし
# ・なるべく英語で書く。絶対に日本語が分からない人が読まないなら日本語でもOK
# ・書くときは文章で書くのが望ましい
# ・# のあとに半角スペースを入れる
# ・インラインコメントはコードのあとに半角スペースを2つ入れて#を書く
# ・Docstringは基本的に全てのmodule, function, class, methodにつける（non publicな外からアクセスしない関数には不要）
# ・そのコードが「なにをしているか」より「なぜそう書いたか」の方が有益

balance = 10000
# 残高が足りない場合を考慮する
if balance > withdraw:
    pass


# 命名規則（naming convention）
# 変数名や関数（メソッド）名：snake_case 例）balance, image_height
# クラス名：CamelCase 例）MyClass
# モジュールやパッケージ名：なるべく短いlower caseで、必須であればsnake_case 例）time, numpy


# アンダースコア
# - _xxx：internal use only(non public)の意味
# - xxx_：Pythonで既に使われている単語を使いたいとき　例）type_
# - __xxx：クラスの属性として使うことで名前修飾される
# - __xxx__：magic methodと呼ばれるもので、Pythonが特別に設定しているもの、開発者定義することはない
# - _：最近実行した戻り値や、iterationに使わない変数
for _ in range(10):
    print('hello!')


# l, I, O：一文字の変数は1や0に見間違えるので使わない
# correct
length = len('letter')

# wrong
l = len('letter')


# Constants（宣言後変更しない変数）は大文字のsnake_caseを使う
PI = 3.14
# 変更できないわけではない
PI = 3


# return
def foo(x):
    if x > 0:
        return math.sqrt(x)
    else:
        return None


# オブジェクトタイプの確認はisinstance()を使う
# correct
if isinstance(obj, int):

# wrong
if type(obj) is type(1):


# Booleanに対して比較演算子を使わない
bool_var = True
# correct
if bool_var:

# wrong
if bool_var == True:


# type hint
def greeting(name: str) -> str:
    return 'Hello ' + name
# 一つでもhintをつけたら全てにつける
# Pythonがtypeのチェックをしてくれるわけではない
# Pythonは動的型付け言語であることを意識
# type hintを強制したり、命名規約入れるべきではない