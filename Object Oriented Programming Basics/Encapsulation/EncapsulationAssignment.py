class Patient:
    def setID(self,ID):
        self.__ID = ID
    def getID(self):
        return self.__ID
    def setName(self,Name):
        self.__Name = Name
    def getName(self):
        return self.__Name
    def setSSN(self,SSN):
        self.__SSN = SSN
    def getSSN(self):
        return self.__SSN
    def display (self):
        print (self.__ID)
        print (self.__Name)
        print (self.__SSN)
c = Patient()
c.setID(123)
c.setName("John")
c.setSSN(5678)
c.display()
