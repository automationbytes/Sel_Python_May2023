mydict = {
    "fruit" :"mango",
    "vegetable":"carrot",
    "name":"devlabs",
    "lang":"python",
    "vegetable": "potato",

}
print(mydict)

#add
mydict["color"] = "Blue"
print(mydict)

#update

mydict.update({"color":"Red"})
print(mydict)


mydict.update({"country":"India",'lang': 'Java'})
print(mydict)

#setdefault - if we hav a key, it will skip; else it wil add
mydict.setdefault("country","US")
print(mydict)

mydict.setdefault("sport","cricket")
print(mydict)

#pop - remove the specified key
mydict.pop("name")
print(mydict)

#popitem - remove the last value
mydict.popitem()
print(mydict)


