from abc import ABC, abstractmethod


class Parent(ABC):
    @abstractmethod
    def marriage(self):
        pass

    def property(self):
        print("house, gold etc")

class Ram(Parent):
    def marriage(self):
        pass

r = Ram()
r.marriage()

class Animal(ABC):

    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Woof..Bow Bow..")

class Cat(Animal):
    def sound(self):
        print("Meow Meow..")

dog = Dog()
dog.sound()
