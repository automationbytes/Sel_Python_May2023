'''
Functions(methods)
Set of lines which will be executed when its being called
Reusability

def functionname(parameters):
    return

'''

def greeting(fname,lname):
    print("Good morning",fname,lname)

greeting("Tom","Jerry")
greeting(fname="Tom",lname="Jerry")
greeting(lname="Jerry",fname="Tom")

def greeting(*name):
    print("Good morning",name[2])
greeting("Tom","Jerry","Jack","Jill")


def greeting(**name):
    print("Good morning",name["two"])
greeting(one = "Tom",two = "Jerry",three= "Jack",four="Jill")

def mycountry(country = "India"):
    print("My country is",country)
mycountry("US")
mycountry()

def add(a,b):
    return a*b

#factorial
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(5))

c = lambda  a,b : a+b
print(c(5,8))

