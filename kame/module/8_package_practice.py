# packageとは
# 複数のPythonモジュールをディレクトリにまとめたもの
# 「.」を使うことでモジュールにアクセスすることができるようになる
# 例）mypackage.mymodule
# 通常ディレクトリに__init__.pyという特殊なファイルを作成することで、そのディレクトリがパッケージとして認識される
# __init__.pyがないと「名前空間パッケージ」として認識される

import myfirstpackage.module1
import myfirstpackage.subdir.module2
myfirstpackage.module1.myfunc()
myfirstpackage.subdir.module2.myfunc()


from myfirstpackage import module1
from myfirstpackage.subdir import module2
module1.myfunc()
module2.myfunc()


from myfirstpackage.subdir.module2 import myfunc
myfunc()


# 名前空間パッケージ（Python3.3以降）
# __init__.pyがないパッケージ
# 異なるパスに存在する同名のパッケージを共通のものとしてまとめることが可能
# 例）/AAA/BBB/myfirstpackage/module1.py　/CCC/DDD/myfirstpackage/module2.py
# 例）import myfirstpackage.module1　import myfirstpackage.module2とすることができる
# 上記は負担がかかるためとくに理由がなければ__init__.pyを作って通常のパッケージとすること

import myfirstpackage
myfirstpackage.myfunc()


from myfirstpackage.subdir import *
myfunc2()


import myfirstpackage.subdir.module2
myfirstpackage.subdir.module2.myfunc2()
