with open("sample1.txt","w") as f:
    f.write("Hello World \n")
    f.write("Good Morning \n")
    f.write("Bye \n")

with open("sample1.txt","r") as f:
    print(f)
    for l in f:
        print(l)

import os
if os.path.exists("Sample1.text"):
    os.remove("Sample1.text")
else:
    print("Not thre")