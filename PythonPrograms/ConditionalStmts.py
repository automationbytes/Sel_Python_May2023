a = 10
b = 5

if (a < b):
    print("A is lesser")
else:
    print("B is lesser")

print("A") if a < b else print("B")

a = 10
b = 5
c = 13

if a > b and a > c:
    print("A is greater")
    print("A is greater")

elif b > a and b > c:
    print("B is greater")
else:
    print("C is greater")

print("A") if a > b and a > c else print("B") if b > a and b > c else print("C")

num = 33
if num > 100:
    print("num is greater than 10")

    if num > 20:
        print("num is greater than 20")

        if num > 30:
            print("num is greater than 30")

            if num > 40:
                print("num is greater than 40")

print("end of if")

'''
numbers - odd/even
numbers - positive/negative
check eligibility for voting
students marklist - m1,m2,m3 
80 -A , 79- 60 - b 59-40 c else f

'''

print("number as input")
a = int(input())
print(a)
if (a == 15):
    print("15 is the numb")