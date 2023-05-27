class calculation:

    num = 2 # class attribute

    def __init__(self,value):
        self.value = value  #instance attribute
        print("Constructor is initiated")

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a,self):
        return a*self.num

calc = calculation(5)
print(calc.value)
