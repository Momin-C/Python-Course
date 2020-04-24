class Student:
    def setID(self,id):
        self.id = id
    def getID(self):
        return self.id
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
s = Student()
s.setID(123)
s.setName("John")
print (s.getID())
print (s.getName())
