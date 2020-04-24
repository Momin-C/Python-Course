class Car:
    def __init__(self,make,year):
        self.make = make
        self.year = year
    class Engine:
        def __init__(self,number):
            self.number = number
        def start(self):
            print ("Engine Started")

c = Car("Tesla",2017)
e = c.Engine(2003)
e.start()
