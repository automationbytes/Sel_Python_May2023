#class attribute

class myclass:
    attr = "Class Attribute"

    @classmethod
    def class_metd(cls):
        print("Class Methods")

print(myclass.attr)


# instance attribute

class instanceclass:
    def __init__(self):
        self.attr = "Instance Attribute"

obj = instanceclass()

#local variable
class localclass:

    def local_metd(self):
        local = "Local Variable"
        print(local)

l = localclass()
l.local_metd()
#print(l.local) #no attribute

global_var = "Global variable"

class globalcls:

    def global_metd(self):
        print(global_var)

l = localclass()
l.local_metd()
print(global_var)