#add - it will simply insert the value(random pos)

vegetables = {"Tomato","Onion","Carrot","Potato","Onion"}
print(vegetables)

vegetables.add("Beetroot")
vegetables.add("Tomato")
print(vegetables)

#update
vegetables = {"Tomato","Onion","Carrot","Potato","Onion"}
fruits = {"apple","mango","pineapple"}

vegetables.update(fruits)
print(vegetables)
print(fruits)

#remove
vegetables.remove("apple")
print(vegetables)

#pop
vegetables.pop()
print(vegetables)

#discard
vegetables.discard("Tomato")
print(vegetables)

#copy
newveg = vegetables.copy()
print(newveg)

#clear
newveg.clear()
print(newveg)
print(len(newveg))
#del
del(newveg)


employee = {"Virat","Sachin","Dhoni"}
student = {"Virat","Tom","Jerry"}
print(employee.intersection(student))
print(employee)
#employee.intersection_update(student)
#print(employee)

print(employee.symmetric_difference(student))

#union
print(employee.union(student))

print(employee.difference(student))
print(student.difference(employee))

#superset/subset
x = {1,2,3,4,5}
y = {1,6}
print(x.issuperset(y))
print(y.issubset(x))

#isdisjoint
vegetables = {"Tomato","Onion","Carrot","Potato","Onion"}
fruits = {"apple","mango","pineapple"}

print(vegetables.isdisjoint(fruits))