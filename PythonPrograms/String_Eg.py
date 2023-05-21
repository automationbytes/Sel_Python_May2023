'''
String - Anythg within single/double quotes

'''

a = "10"
b = "Hello"
c = '10'
d = 'Hello'
print(type(b))
print(type(d))

multi = "Python is more easy to learn " \
        "and simple to use programming language" \
        "python offers more customizationpython is powerful" \
        "And it is general purpose language"

print(multi)

#len
a = "SACHIN"
print(len(a))

#indexing - char at any index
print(a[4])
#negative indexing
print(a[-4])

#slicing - cuttingdown the string into substring
print(a[2:4])

a = "Aeroplane is flying high"
print(a[2:8])
print(a[2:24:2])
print(a[:6])
print(a[2:])
print(a[:])
print(a[::-1])


#Strip
a = "     Hello World    "
print(a.strip())
print(a.rstrip())
print(a.lstrip())

#upper/lower
b = "Basketball"
print(b.upper())
print(b.lower())
print(b.casefold())

c = "GRAß"
print(c.lower())
print(c.casefold())

d = "DanCeR"
print(d.swapcase())

e = "good morning everyone"
print(e.capitalize())
print(e.title())

f = "Your booking id is : 54897"
sp = f.split(":")
print(sp[0])
print(sp[1].strip())
print(type(sp))

#concat
a = "Apple"
b = "phone"
print(a+" "+b)

c = 5
print(a+format(c))
print(a+str(c))

txt = "My dog name is {0} and he is {1} year old".format("Tommy",2)
print(txt)


txt = "My dog name is {name} and he is {age} year old".format(name="Tommy",age = 2)
print(txt)

t = "your transcation id is : {567497}"
startindex = t.find("{")+1
endindex = t.find("}")
print(t[startindex:endindex])

txt = "I love apple, apple is my fav fruit. even I hav apple phone"
print(txt.count("apple"))

a = ["Sachin","Ganguly","Dhoni","Virat"]
x = "* ".join(a)
print(a)
print(x)
print(type(a))
print(type(x))

txt = "76797"
print(txt.zfill(16))

