class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f'{self.name} съел {food.name}')
                self.fed = True
            else:
                print(f'{self.name} не стал есть {food.name}')
                self.alive = False
        else:
            print(f'{self.name} не может съесть это!')


class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False


class Mammal(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.type = 'Млекопитающее'


class Predator(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.type = 'Хищник'


class Flower(Plant):
    # noinspection PyArgumentList
    def __init__(self, name):
        Plant.__init__(self, name)
        self.edible = False


class Fruit(Plant):
    # noinspection PyArgumentList
    def __init__(self, name):
        Plant.__init__(self, name)
        self.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)
