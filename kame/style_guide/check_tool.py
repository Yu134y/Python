# Style Guideをチェックする(Linter)
# Pycharmでチェックする
import os, sys
x =1
y =2
print          (x, y, z)


# Linterの種類
# Stylistic Lint
# 例：一行で二つのモジュールをimportしている！
# import os, sys
# 代表的なlinter:pycodestyle(元pep8)

# Logical Lint
# 例：使われていないモジュールがimportされている！
# import sys
# 代表的なlinter:pyflakes

# pycodestyleとpyflakesのラッパーライブラリ:flake8
# flake8より厳しい:pylint
