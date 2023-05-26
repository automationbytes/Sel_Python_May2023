class Google:
    def __init__(self,username,locationlogged):
        self.username = username
        self.locationlogged = locationlogged

    def toDisplay(self):
        print(self.username)
        print(self.locationlogged)

class Youtube(Google):
    def __init__(self,username,locationlogged,channelname):
        super().__init__(username,locationlogged)
        self.channelname = channelname

    def toDisplay(self):
        super().toDisplay()
        print(self.channelname)

y = Youtube("Devlabs","India","Devops University")
y.toDisplay()