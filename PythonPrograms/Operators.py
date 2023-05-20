'''

Operators - used to perform any operations on variables/value

Arthimetic Operators


'''

#Arthimetic Operators - to perform basic math operations

a = 5
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b) #float
print(a//b) # floor division - int - quotient - which is without decimal point
print(a%b) #mod - remainder
print(a**b) #exponential - 5**3 = 5*5*5

#Comparison operators - comparing two values
a = 5
b = 3

print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)

#Assignment - Assign the values back to variables

p = 5
#p = p + 5
p += 5
print(p)

#Logical operator - more than one operations

'''
and
---

true and true = true
true and false = false
false and true = false
false and false = false

or
--

true or true = true
true or false = true
false or true = true
false or false = false

not
---
true -> false
false - true
'''

a = 1
b = 5
c = 3
print("And Operator")
print(a<b and a>c)

print("OR Operator")
print(a<b or a>c)


print("NOT Operator")
print(not(a<b) or a>c)



#Increment Operator
#a++

a = a+1
a +=1

#Bitwise operator

'''
&
--
1 & 1 = 1
1 & 0 = 0
0 & 1 = 0
0 & 0 = 0

|
1 | 1 = 1
1 | 0 = 1
0 | 1 = 1
0 | 0 = 0

'''


a = 1 # 001
b = 5 # 101
c = 4 # 100
      # ---
        #101
print(c & b) # 001 # 1
print(c | b) #101 #4+0+1

#Identity operators

fruits = ["Apple","Mango","Banana","Stawberry"]
newfruits = ["Apple","Mango","Banana","Stawberry"] # new
NFruits = fruits
# NFruits = NFruits.pop()
# print(NFruits)
print(fruits is newfruits) #false - they both are seperate objects in memry
print(fruits is NFruits) # true - becoz its refers to same list object
print(fruits == newfruits) # true - bcoz we are just comparing the values of the list


#Membership operators

fruits = ["Apple","Mango","Banana","Stawberry"]
print("Banana" in fruits)
print("Blueberry" not in fruits)