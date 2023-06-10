class Employee:
    def __init__(self, firstname,lastname,city,country,street,zipcode,eid):
        self.firstname = firstname
        self.lastname = lastname
        self.city = city
        self.country = country
        self.street = street
        self.zipcode = zipcode
        self.eid = eid
    def mydict(self):
        return {

                "address": {
                    "city": self.city,
                    "country": self.country,
                    "street": self.street,
                    "zipCode": self.zipcode
                },
                "firstName": self.firstname,
                "lastName": self.lastname,
                "eid":self.eid
        }