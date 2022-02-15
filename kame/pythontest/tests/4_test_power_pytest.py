# pytest
# pythonのテストフレームワークで、多くのプロジェクトが採用している
# python標準のassertを使って簡潔に書ける
# $pip install pytestでインストールする
# ターミナルでpytest <ファイル名> -v
# テストカバレッジ：ターミナルでpytest <ファイル名> --cov=power (どの行かわかる：--cov-report term-missing)


import pytest
from pythontest.power import power, times, divide


def test_power():
    base = 2
    exp = 3
    assert power(base, exp) == 8
    with pytest.raises(TypeError):
        power('3', '2')


def test_times():
    num1 = 2
    num2 = 3
    assert times(num1, num2) == 6


def test_divide():
    num1 = 4
    num2 = 2
    assert divide(num1, num2) == 2


def test_divide_by_zero():
    num1 = 4
    num2 = 0
    assert divide(num1, num2) is None
