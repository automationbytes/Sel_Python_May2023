'''

Set is very similar to set in other language
set is mutable (Modifiable)
Insertion order is not maintained
So indexing not be allowed
Set doesnt allows duplicates
Set can contain both hetro and homo data (Same/ diff data type)
{}

'''

vegetables = {"Tomato","Onion","Carrot","Potato","Onion"}
print(vegetables)

vegetables = ["Tomato", "Onion", "Carrot", "Potato", "Onion"]
veggies = set(vegetables)
print(veggies)
print(type(veggies))

for v in veggies:
    print(v)

for i in range(len(veggies)):
    print(veggies[i])