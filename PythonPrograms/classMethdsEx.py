class calculationclass:

    num = 2 # class attribute

    def __init__(self,value):
        self.value = value  #instance attribute
        print("Constructor is initiated")

    @classmethod
    def mul(cls,a):
        return a * cls.num

print(calculationclass.mul(4))

class calculationstatic:

    num = 2 # class attribute

    def __init__(self,value):
        self.value = value  #instance attribute
        print("Constructor is initiated")

    @staticmethod
    def mul(a):
        return a

print(calculationstatic.mul(4))



class calculationwithout:

    num = 2 # class attribute

    def __init__(self,value):
        self.value = value  #instance attribute
        print("Constructor is initiated")

    def mul(self,a):
        return a * self.num * self.value
c = calculationwithout(5)
print(c.mul(4))
