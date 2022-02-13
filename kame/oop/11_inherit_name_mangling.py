class Person:
    def __init__(self, name):
        self.name = name
        self.__my_method()

    def my_method(self):
        print('Person method is called')

    __my_method = my_method


class Baby(Person):
    def my_method(self):
        print('Baby method is called')
    pass


taro_baby = Baby('Taro')  # Person method is called
taro_person = Person('Taro')  # Person method is called
taro_person.my_method()  # Person method is called
print(taro_baby.name)
taro_baby.my_method()  # Baby method is called
print(dir(taro_baby))
