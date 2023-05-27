class myclass:

    attr = "Public attribute"

    def public_metd(self):
        print("Public Methd")

obj1 = myclass()
print(obj1.attr)
obj1.public_metd()

class privclass:

    __attr = "private attribute"

    def __priv_metd(self):
        print("private Methd")

obj1 = privclass()
print(obj1.__attr)
obj1.__priv_metd()




class prdvclass:

    _attr = "prd attribute"

    def _priv_metd(self):
        print("prd Methd")

obj1 = prdvclass()
print(obj1._attr)
obj1._priv_metd()
