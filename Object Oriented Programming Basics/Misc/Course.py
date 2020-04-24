class Course:
    def __init__(self,name,grades):
        self.name = name
        self.grades = grades
    def average(self):
        numberOfGrades= len(self.grades)
        average = sum(self.grades)/numberOfGrades
        print ("Average Grades for:",self.name,"is:",average)

c1 = Course("Momin",[1,2,3,4,5])
print (c1.name)
print (c1.grades)
c1.average()

c2 = Course("Java Web Services",[5,5,5,5,5])
print (c2.name)
print (c2.grades)
c2.average()
