'''

Tuple is very similar to array in other language
Tuple is immutable (unmodifiable)
Insertion order is maintained
Random Access
allows duplicates
Index to access the values
can contain both hetro and homo data (Same/ diff data type)
() - without brackets
'''

fruits = ("Apple","Banana","Stawnberry","Grapes")
print(fruits)
print(type(fruits))


fruits = "Apple","Banana","Apple","Stawberry","Grapes","Apple"
print(fruits)
print(type(fruits))

#indexing
print(fruits[2])

#negative indexing
print(fruits[-2])

#Slicing
print(fruits[1:3])

#negative slicing
print(fruits[-3:-1])

print(fruits.count("Apple"))

print(fruits.index("Stawberry"))


#add/update
fruits = ("Apple","Banana","Stawnberry","Grapes")
newfruits = list(fruits)
newfruits.append("Papayya")
print(newfruits)
fruits = tuple(newfruits)
print(fruits)

#
fruits = {"Apple","Banana","Stawberry","Grapes"}
sorted_set = sorted(fruits)
print(sorted_set)
print(type(sorted_set))
