class Person(object):  # クラス名はCamelCase

    num_legs = 2
    count = 0

    # constructor
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Person.count += 1

    def walk(self):
        print(f'{self.name} is walking... with {Person.num_legs} legs!')

    def run(self):
        print(f'{self.name} is running... with {Person.num_legs} legs!')


# クラス名()で__init__が呼ばれる
john = Person('John', 28, 'male')
print(Person.count)
taro = Person('Taro', 18, 'male')
print(Person.count)
emma = Person('Emma', 40, 'female')
print(Person.count)

# インスタンス変数（インスタンスに紐づく変数）
# 「.」に続けてアクセス可能
print(john.name)
print(john.age)
print(john.gender)

print(taro.name)
print(taro.age)
print(taro.gender)

print(f'変更前：{john.age}')
john.age = 29
print(f'変更後：{john.age}')

# インスタンスメソッド
john.walk()
emma.walk()
taro.run()

# クラス変数（インスタンスに紐づかない変数）
print(john.num_legs)
print(taro.num_legs)

print(Person.num_legs)
print('Person.num_legs = 3を実行')
Person.num_legs = 3
print(john.num_legs)
print(taro.num_legs)
print(emma.num_legs)

print('john.num_legs = 4を実行')
john.num_legs = 4  # バグのもとになるので基本的には使わない
print(john.num_legs)
print(taro.num_legs)
print(emma.num_legs)