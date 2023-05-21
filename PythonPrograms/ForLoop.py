#start stop step - #init condition increment
'''
Always remember start should be small
        and stop should be bigger if my step is positive

'''
for i in range(10,100,5):
    print(i)

print("***********************")

for i in range(100,-1,-2):
    print(i)

print("***********************")

a = "Sachin"
for i in range(0,len(a),1):
    print(a[i])


a = ["Sachin","Ganguly","Dhoni","Virat"]
for i in range(0,len(a),1):
    print(i,a[i])

print("***********************")
#start = 0 and step = 1
for i in range(len(a)):
    print(a[i])

print("***********************")
#start = 0 and step = 1
for i in range(10):
    print(i)

print("***********************")
#step = 1
for i in range(5,10):
    print(i)

#start = 0 and step = 1
for i in range(10):
    print(i)
    if i == 5:
        break

