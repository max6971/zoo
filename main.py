class Aninals():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} кушает")


class Bird(Aninals):

    def make_sound(self):
        print("карр карр")


class Mammal(Aninals):

    def make_sound(self):
        print("мяу")


class Reptile(Aninals):

    def make_sound(self):
        print("ква ква")


def animals_sound(animals):
    for animal in animals:
        animal.make_sound()


class Zoo():
    def __init__(self):
        self.animals = []
        self.sotrudniki = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк")

    def add_sotrudniki(self, new_sotrudnik):
        self.sotrudniki.append(new_sotrudnik)
        print(f"Сотрудник {new_sotrudnik.name} добавлен в штат зоопарка")


class ZooKeeper():
    def feed_animal(self, animal):
        print(f"сотрудник кормит {animal.name} ")


class ZooVeterinarian():
    def lechit_animal(self, animal):
        print(f"Ветеринар лечит {animal.name} ")


bird1 = Bird("воробей", 1)
bird2 = Bird("воробушек", 2)
mammal1 = Mammal("кот", 5)
mammal2 = Mammal("котик", 1)
reptile1 = Reptile("лягушка", 1)
reptile2 = Reptile("жаба", 3)

zoo = Zoo()
keeper = ZooKeeper()
veterinarian = ZooVeterinarian()

zoo.add_animal(bird1)
zoo.add_animal(mammal2)
zoo.add_animal(reptile1)

zoo.add_sotrudniki(keeper)
zoo.add_sotrudniki(veterinarian)

animals_sound(zoo.animals)

keeper.feed_animal(reptile1)
keeper.feed_animal(mammal2)
veterinarian.lechit_animal(bird1)
