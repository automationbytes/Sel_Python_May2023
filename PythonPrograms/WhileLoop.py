i = 1
while i < 10:
    print(i)
    i += 1

#reverse it
num = 1234 #4321
reversenum = 0

while num > 0:
    remainder = num % 10 #1234%10 = 4; 123%10=3
    reversenum = reversenum * 10 + remainder #0*10+4; 4*10+3;43*10+2..
    num = num // 10 #123
print(reversenum)

num1 = 1234
numstr = str(num1)
z = int(numstr[::-1])
print(z)


