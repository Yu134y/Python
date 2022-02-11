# キャスティング（casting）：データ型の変換

# strings  '1'
# int  1
# float  1.0
# boolean  True, False
# list  [1, 2, 3, 4, 5]
# tuple  (1, 2, 3)
# dictionary  {'one': 1, 'two': 2, 'three': 3}
# set  {1, 2, 3, 4, 5}

# str(), int(), float(), list(), bool(), tuple(), set()
print(type(str(1)))
print(type(int(1)))
print(1 + int('1'))
print(str(1) + '1')
print(float('1'))
print(list('hello'))
print(bool(1))
print(bool(0))
print(tuple([1, 2, 3, 4]))
print(set([1, 2, 3, 3, 4, 5, 5, 5]))
