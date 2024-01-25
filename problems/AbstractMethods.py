from abc import ABC, abstractmethod
# appling animals example herbervore and carnivore
class Animal(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def move(self):
        pass
    @abstractmethod
    def make_sound(self):
        pass
class Herbivore(Animal):
    def __init__(self, name):
        super().__init__(name)
    def move(self):
        print(f'{self.name} is running')
    def make_sound(self):
        print(f'{self.name} is making sound')
class Carnivore(Animal):    
    def __init__(self, name):
        super().__init__(name)
    def move(self):
        print(f'{self.name} is running')
    def make_sound(self):
        print(f'{self.name} is making sound')
dog = Carnivore('Dog')
dog.move()