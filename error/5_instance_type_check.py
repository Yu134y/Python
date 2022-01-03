class Animal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f'{self.name} is walking!!')


class Dog(Animal):
    def bark(self):
        print(f'{self.name} is barking!!')


def walk_with_me(animal: Animal) -> None:
    # if type(animal) is Animal:
    # if isinstance(animal, Animal):
    method = getattr(animal, 'walk', None)
    if callable(method):
        animal.walk()
    else:
        raise TypeError(f'{type(animal).__name__}は散歩(walk)できません')


if __name__ == '__main__':
    pochi = Dog('Pochi')
    walk_with_me(pochi)