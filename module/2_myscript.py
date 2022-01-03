# 標準ライブラリ、サードパーティのライブラリ、自分たちのライブラリ、ローカルのライブラリの順にインポートする
# abc順
# 各ライブラリごとに一行開ける

import sys
sys.path.append('C:\\Users\\y_ono\\PycharmProjects\\PythonLecture\\function')

import docstring_15
import mymodule_1 as mm  # asは非推奨
from mymodule_1 import myfunc, myvariable, anotherfunc
# from mymodule_1 import *  # 全てにアクセスできるようになるが何がインポートされているかわからないため非推奨
mm.myfunc()
print(mm.myvariable)
mm.anotherfunc()

myfunc()
print(myvariable)
anotherfunc()

print(sys.path)
print(docstring_15.multiply(3, 4))