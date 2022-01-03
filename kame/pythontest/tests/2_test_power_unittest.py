# Test runner
# テスト結果をチェックしてくれたり、デバッグしやすいように結果を表示してくれる
# unittestとpytest
# ・unittest：Python標準でスタンダード
# ・pytest：テストフレームワーク。非常に有名で多くのプロジェクトで利用されている

import unittest
from power import power, times


class TestMyMethod(unittest.TestCase):
    def test_power(self):
        base = 2
        exp = 3
        self.assertEqual(power(base, exp), 8)

    def test_times(self):
        num1 = 2
        num2 = 3
        self.assertEqual(times(num1, num2), 6)


if __name__ == '__main__':
    unittest.main()
# ターミナルでは、python -m unittest <ファイル名>で実行する
