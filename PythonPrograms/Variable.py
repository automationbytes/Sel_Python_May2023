'''

Variables- Identifier/Container to store some values

Starts with an Alphabets/underscore
Only spl char allowed is underscore
Should nt starts wit number
should nt hav any spaces

variables are case sensitive

Datatype- type of data wat the variables holds

numbers - int, float, complex
String - str
boolean - bool - True/False

Sequence Types - list, tuple, range
Mapping types - dict
Set types - set, frozen set
====================================
Binary types- bytes, byte array, memory view
None type - none
'''

a,b = 10,20.59

print(a)
print(b)
print(type(a))
print(type(b))

#complex - it includes real n imaginary part
c = 5+88j
print(c)
print(type(c))

#String
d = "Hello"
e = 'Hello'
print(type(d))
print(type(e))

#list
al = ["apple","ball","cat"]
print(al)

#tuple
tl = ("apple","ball","cat")
print(tl)

#set
s = {5,7,9}
print(s)
#dict
d = {
    'a': "apple",
    "b":'ball',
    "c":"cat"
}

print(d)
print(type(d))
x = None
print(type(x))

z = bytearray(5)
print(z)
print(type(z))

m = memoryview(bytes(3))
print(m)
print(type(m))




