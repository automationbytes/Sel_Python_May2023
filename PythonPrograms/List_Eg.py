'''

List is very similar to array in other language
List is mutable (Modifiable)
Insertion order is maintained
Random Access
List allows duplicates
Index to access the values
List can contain both hetro and homo data (Same/ diff data type)
[]

'''

fruits = ["Apple", "Mango", "Banana", "Stawberry", "Mango"]
print(fruits)

#length
print(len(fruits))

#indexing - its start with 0
print(fruits[2]) #Banana

#Negative Indexing - Its last from last value (-1)
print(fruits[-1])

#slicing - Cutting down the list into pieces based on index
print(fruits[1:4]) # 1,2,3 values not the 4 - always the upper bound wil nt b considered

#negative Slicing
print(fruits[-3:-1])

#slicing wit step
print(fruits[1:4:2])

print(fruits[:-3])
print(fruits[-3:])
print(fruits[:4])
print(fruits[2:])

#reversing the list
print(fruits[::-1])

#mixed list
mixval = ["Apple","Ball",3,"Elephant",5.5]
print(mixval)

#['Apple', 'Mango', 'Banana', 'Stawberry', 'Mango']
#for each loop
for f in fruits:
    print(f)

for i in range(0,len(fruits),1):
    print(fruits[i])

print(type(fruits))
