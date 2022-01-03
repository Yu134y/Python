import time


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_from_dob(cls, name, year, month, date):
        today = time.localtime()
        # if (today.tm_mon, today.tm_mday) < (month, date):
        #     age = today.tm_year - year - 1
        # else:
        #     age = today.tm_year - year
        age = today.tm_year - year - ((today.tm_mon, today.tm_mday) < (month, date))
        return cls(name=name, age=age)


john = Person('John', 20)
emma = Person.create_from_dob('Emma', 1989, 12, 30)
print(john.name)
print(emma.name)
print(emma.age)
print(type(john))