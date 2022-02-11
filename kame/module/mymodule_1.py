my_variable = 'This is global variable'


def my_func():
    print('This is my function!!')


def another_func():
    print('This is another function!!')


if __name__ == '__main__':
    my_func()
    another_func()
    print(my_variable)
    print('This is my module!!')
