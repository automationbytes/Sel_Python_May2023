'''

Everything in python is an object, which has its own properties and method

Student
    #attributes
    name
    mobilenum

    #methods
    study
    writing

'''

class Student:
    name = "Tom"
    mobnum = 123456789

    def studying(self):
        print("Study method of",self.name)

    def calling(self):
        print("Call to mobile method of",self.mobnum)

s = Student()
s.studying()
s.calling()
print(s.name)

class student:
    schoolname = "Devops University"
    def __init__(self,name,mobnum):
        self.name = name
        self.mobnum = mobnum

    def studying(self,schoolname):
        print(schoolname,"Study method of",self.name)

    def calling(self):
        print("Call to mobile method of",self.mobnum)

s1 = student("Tom",123456789)
s2 = student("Jack",987456123)
s1.calling()
s2.calling()
s1.studying("DevopsUniv")

print(s1.schoolname)
print(s2.schoolname)
student.schoolname = "Devlabs"
print(s1.schoolname)
print(s2.schoolname)

