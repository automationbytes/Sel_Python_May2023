'''

File Handling - creating reading, updating and deleting

Open(filename,modes)
#read - r
append - a
write - w
create -x
text - t
binary - b
'''

#f = open("sample.txt","x")


f = open("sample.txt","w")
f.write("To write something on file")
f.close()

f = open("sample.txt","r")
print(f.read())


f = open("sample.txt","a")
f.write("\n Append statement. This will nt over write")
f.close()

f = open("sample.txt","r")
print(f.read())

