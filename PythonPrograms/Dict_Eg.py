'''

Dict - Use key and value pair
mutable
ordered - 3.7
duplicate key is not allowed
{}


'''

mydict = {
    "fruit" :"mango",
    "vegetable":"carrot",
    "name":"devlabs",
    "lang":"python",
    "vegetable": "potato",

}
print(mydict)

#access the dict
print(mydict["fruit"])
print(mydict.get("fruit"))

#len
print(len(mydict))

#loop
#key
for k in mydict.keys():
    print(k)

#values
for v in mydict.values():
    print(v)

for k in mydict.keys():
    print(mydict[k])

#both key and value
for k in mydict.items():
    print(k)

print(mydict.items())
print(type(mydict.items()))
print(type(mydict.keys()))

newdic = mydict.copy()
print(newdic)

newdic.clear()
print(newdic)

del(newdic)




mydict = {
    "fruit" :"mango",
    "vegetable":"carrot",
    "name":"devlabs",
    "lang":"python",
    "vegetable": "potato",

}
#
# for i in sorted(mydict.keys(),reverse=True):
#     print(i,mydict[i])

newdic = dict(sorted(mydict.items()))
print(newdic)

print(sorted(mydict))

# mykeys = list(mydict.keys())
# mykeys.sort()
# print(mykeys)
# sorted_dict = {i : mydict[i] for i in mykeys}
# print(sorted_dict)
#
# from collections import OrderedDict
# dic = OrderedDict(sorted(mydict.items()))
# print(dic)
#
