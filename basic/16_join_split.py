# join

# 'Hi My name is John'
text = ' '.join(['Hi', 'My', 'name', 'is', 'John'])
print(text)

# split(リストで返す）
print('Hi My name is John'.split(' '))
print('Hi My name is John'.split())  # デフォルトは半角スペースをカット

filename = 'sample.py'
print(filename.split('.')[0])
print(filename.split('.')[-1])