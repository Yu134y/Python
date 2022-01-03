# ジェネレータ（generator）
# メモリを節約する仕組み
# 全てのデータをメモリに置く代わりに、イテレーション時に毎回出力する（HDから取得したり、計算したり、もしくはその両方）

import csv
import sys

range_nums = range(20)
# for i in range_nums:
#     print(i)

# list_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
list_nums = list(range_nums)
print(list_nums)
# for i in list_nums:
#     print(i)

print(sys.getsizeof(range_nums))
print(sys.getsizeof(list_nums))

with open('example.csv') as f:
    reader = csv.DictReader(f)
    print(sys.getsizeof(reader))
    for line in reader:
        print(line)
