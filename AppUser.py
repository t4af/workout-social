class AppUser():

    def __init__(self, userName, password, totalPoints):
        self.userName = userName
        self.password = password
        self.totalPoints = totalPoints

    def setUserName(self, name):    # sets username
        self.userName = name

    def setUserPass(self, pw):      # sets password
        self.password = pw

    def getUserName(self):          # retrieves username
        return self.userName

    def addPoints(self, points):    # adds points to point total
        self.totalPoints = self.totalPoints + points

    def getPoints(self):
        return self.totalPoints     # returns totalPoints

