class Dog():
    def sound(self):
        print("Woof..Bow Bow..")
    def use(self):
        print("To bark at strangers")

class Cat():
    def sound(self):
        print("Meow Meow..")
    def food(self):
        print("Drink milk")

class Animal(Cat,Dog):
    def display(self):
        print("Hello")


class Man(Animal):
    def speak(self):
        pass
dog = Man()
dog.sound()
dog.food()
