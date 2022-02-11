# 標準ライブラリ、サードパーティのライブラリ、自分たちのライブラリ、ローカルのライブラリの順にインポートする
# abc順
# 各ライブラリごとに一行開ける

import sys
sys.path.append('C:\\Users\\y_ono\\PycharmProjects\\PythonLecture\\function')

import docstring_15  # sys.pathに追加されるのはスクリプトが実行されてからのため、コード記述時ではdocstring_15がなくエラーが出ている
import mymodule_1 as mm  # asは非推奨
from mymodule_1 import my_func, my_variable, another_func
# from mymodule_1 import *  # 全てにアクセスできるようになるが何がインポートされているかわからないため非推奨

mm.myfunc()
print(mm.myvariable)
mm.anotherfunc()

my_func()
print(my_variable)
another_func()

print(sys.path)
print(docstring_15.multiply(3, 4))
