fruits = ['Apple', 'Mango', 'Banana', 'Stawberry', 'Mango']
vegetables = ["Tomato","Onion","Carrot","Potato","Onion"]

#append - add a single value to the list, it will add the values at the end of the list
fruits.append("Orange")
print(fruits)

#fruits.append(vegetables)
#extend - two list- and combine into one
fruits.extend(vegetables)
print(fruits)

#insert - inserting value in specified index
fruits.insert(2,"Grapes")
print(fruits)

#Remove
fruits.remove("Onion")
print(fruits)

#pop - this remove last items
fruits.pop()
print(fruits)

#pop - with index
fruits.pop(6)
print(fruits)

#copy
newfruits = fruits.copy()
print(newfruits)

#clear - empty the list
newfruits.clear()
print(newfruits)

#del
del(newfruits)
#print(newfruits)

#sorting
vegetables.sort()
print(vegetables)

#descending order
vegetables.sort(reverse=True)
print(vegetables)

#reverse
fruits.reverse()
print(fruits)


#Remove duplicates from a given list
#find the sum of elements
#count the occurrences of element
#min and max value in the list

num = [5,7,8,3]
sum = 0
for n in num:
    sum = sum + n
print(sum)
#
# print(max(num))
# print(min(num))
#

num.sort()
print(num)
print(num[0])
print(num[-1])

#length of list
num = [5,7,8,3]
sum = 0
for n in num:
    sum = sum + 1
print(sum)
