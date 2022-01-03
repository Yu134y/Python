# built in function

# type() 値の種類を返してくれる
# 関数が返してくれる値を戻り値、返り値という
hello_type = type('Hello')
print(hello_type)
print(type(1))

# id()
hello_id = id('hello')
print(hello_id)

# 文字列が同じだと変数が違くても返すidは一緒
hello = 'hello'
hello2 = 'hello'
print(id(hello))
print(id(hello2))

w = 'world'
print(id(w))
print(id('world'))
