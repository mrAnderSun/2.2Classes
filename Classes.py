class Animals:  # Класс/словарь животных
    animals_weight = {}

    def sum_animal_weights(self):
        self.animals_weight.update([(self.name, self.weight)])
        return self.animals_weight

#####
class Goose(Animals):  # Гуси
    def __init__(self, name="Amundsen", weight=1):
        self.name = name
        self.weight = weight

    def eat(self):
        print(f'{self.name} eaten')

    def voice(self):
        print("Ga-Ga-Ga-Ga")

    def setting(self):
        print(f'{self.name} give eggs')

#####
class Cow(Goose):  # Корова

    def milk(self, milk=10):
        print(f'Cow {self.name} give milk')

    def voice(self):
        print("Mou-Mou")

#####
class Sheep(Goose): #Овца

    def fleece(self):
        print(f'Sheep {self.name} give silk')

    def voice(self):
        print("Uka-Chaka-Uka-Uka..Uka_Chaka")

#####
class Chicken(Goose):

    def voice(self):
        print("Kuka-Rek-Kuoo")

#####
class Goat(Cow):

    def voice(self):
        print("Bhe-Bhee-Bheee")

#####
class Duck(Chicken):

    def voice(self):
        print("Krya-krya")

#####
ferma = []
milk = []
fleece = []
setting = []
my_animal_goose1 = Goose("Рэмбо", 16)
my_animal_goose1.sum_animal_weights()
ferma.append(my_animal_goose1)
setting.append(my_animal_goose1)

my_animal_goose2 = Goose("Чак", 18)
my_animal_goose2.sum_animal_weights()
ferma.append(my_animal_goose2)
setting.append(my_animal_goose2)

my_animal_cow1 = Cow("Жасмин", 120)
my_animal_cow1.sum_animal_weights()
ferma.append(my_animal_cow1)
milk.append(my_animal_cow1)

my_animal_sheep1 = Sheep('Шон', 40)
my_animal_sheep1.sum_animal_weights()
ferma.append(my_animal_sheep1)
fleece.append(my_animal_sheep1)

my_animal_sheep2 = Sheep("Люк", 50)
ferma.append(my_animal_sheep2)
my_animal_sheep2.sum_animal_weights()
fleece.append(my_animal_sheep2)

my_animal_chicken1 = Chicken("Оби Ван", 5)
my_animal_chicken1.sum_animal_weights()
ferma.append(my_animal_chicken1)
setting.append(my_animal_chicken1)

my_animal_chicken2 = Chicken("Йода", 7)
my_animal_chicken2.sum_animal_weights()
ferma.append(my_animal_chicken2)
setting.append(my_animal_chicken2)

my_animal_goat1 = Goat("Кайл Ривз", 14)
my_animal_goat1.sum_animal_weights()
ferma.append(my_animal_goat1)
milk.append(my_animal_goat1)

my_animal_goat2 = Goat("Тайлер Дерден", 16)
my_animal_goat2.sum_animal_weights()
ferma.append(my_animal_goat2)
milk.append(my_animal_goat2)

my_animal_duck1 = Duck("Ганнибал", 12)
my_animal_duck1.sum_animal_weights()
ferma.append(my_animal_duck1)
setting.append(my_animal_duck1)

#####
def eat():
    for animal in ferma:
        animal.eat()

#####
def voices():
    for animal in ferma:
        animal.voice()

#####
def massa():

    print(f'result of summation mass animals = {sum(Animals.animals_weight.values())}')
    for k, v in Animals.animals_weight.items():
        if v == max(Animals.animals_weight.values()):
            print(f'max mass animal: '
                  f'{k} = {max(Animals.animals_weight.values())}')

#####
def food():

    #for animal in milk:
     #   print(animal)
      #  print(animal.milk())
    print(setting)
    for animal1 in setting:
        #print(animal)
        print(animal1.setting())
    for animal2 in fleece:
        #print(animal)
        print(animal2.fleece())
    for animal3 in milk:
        #print(animal)
        print(animal3.milk())

#####
while True:
  operation = input("What do you want? \n")
  if operation.title() == "E":
    eat()
  elif operation.title() == "V":
    voices()
  elif operation.title() == "M":
    massa()
  elif operation.title() == "F":
    food()
  elif operation.title() == "Q":
      break