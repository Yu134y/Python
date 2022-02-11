# Decorator：関数に機能を付属する（デコレートする）
def greeting(func):
    def inner(*args, **kwargs):
        print('Hello!')
        func(*args, **kwargs)
        print('Nice to meet you!')
    return inner


@greeting
def say_name(name):
    print(f'I\'m {name}')


@greeting
def say_name_and_origin(name, origin):
    print(f"I'm {name}, I'm from {origin}")


# say_name = greeting(say_name)
say_name('Jiro')
say_name_and_origin('Taro', 'Tokyo')
