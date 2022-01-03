# 例外ケースのテスト
# 謝ったデータを入れたらきちんとエラーを返すかをテストする
# 考えられる例外は無数に出てくるので、ある程度絞ってテストをする
# withステートメントを使ってテストする

import unittest
from power import power, times


class TestMyMethod(unittest.TestCase):
    def test_power(self):
        base = 2
        exp = 3
        self.assertEqual(power(base, exp), 8)
        # context manager
        with self.assertRaises(TypeError):
            power('3', '2')

    def test_times(self):
        num1 = 2
        num2 = 3
        self.assertEqual(times(num1, num2), 6)


if __name__ == '__main__':
    unittest.main()
