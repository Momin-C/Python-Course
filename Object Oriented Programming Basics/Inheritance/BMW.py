from abc import abstractmethod,ABC
class BMW(ABC):
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass

class ThreeSeries(BMW):
    def __init__(self,cruiseControl,make,model,year):
        super().__init__(make,model,year)
        self.cruiseControl = cruiseControl
    def display():
        print (self.cruiseControl)
    def start(self):
        super().start()
        print ("Button start")
    def stop(self):
        super().stop()
        print ("Button stop")
    def drive(self):
        print ("Three Series is being Driven")

class FiveSeries(BMW):
    def __init__(self,parkingAssist,make,model,year):
        super().__init__(self,make,model,year)
        self.parkingAssist = parkingAssist
    def drive(self):
        print ("Five Series is being Driven")
    def start(self):
        super().start()
        print ("Remote start")
    def stop(self):
        super().stop()
        print ("Remote stop")

bmw = ThreeSeries(True,"Tesla","Model 3","2020")
bmw.start()

print (bmw.cruiseControl)
print (bmw.make)
print (bmw.model)
print (bmw.year)
