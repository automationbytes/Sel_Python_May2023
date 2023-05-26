'''
Inheritance - allow us to define a class that inherits all methods/properties
Parent class -
Child class

'''

class Google:
    def loginpage(self):
        print("Login page of Google")
    def homePage(self):
        print("Home page of Google")

class Youtube(Google):
    def toPlay(self):
        print("Play videos")

y = Youtube()
y.toPlay()
y.loginpage()


class Parent:
    def marriage(self):
        print("Marry Sita")

    def property(self):
        print("house, gold etc")

class Ram(Parent):
    def marriage(self):
        super().marriage()
       # print("Marry Lakshmi")

r = Ram()
r.marriage()