'''

try - let us to execute block of code with errors
except - catch - to handle the errors
finally - regardless of try/except
else - when there is no error it will be executed

'''
a = 1
import traceback
try:
    print(a)
except NameError:
    print("variable s nt defined")
except:
    print("Exception occured")
    traceback.print_exc()
else:
    print("Else")
finally:
    print("Finally")


age = 5
if age < 18:
    raise Exception("Not Eligible for voting")