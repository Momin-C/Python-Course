class BMW:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def start(self):
        print ("Starting the car")
    def stop(self):
        print ("Stopping the car")

class ThreeSeries(BMW):
    def __init__(self,cruiseControl,make,model,year):
        super().__init__(make,model,year)
        self.cruiseControl = cruiseControl
    def display():
        print (self.cruiseControl)
    def start(self):
        super().start()
        print ("Button start")

class FiveSeries(BMW):
    def __init__(self,parkingAssist,make,model,year):
        super().__init__(self,make,model,year)
        self.parkingAssist = parkingAssist
ThreeSeries = ThreeSeries(True,"Tesla","Model 3","2020")
ThreeSeries.start()
"""
print (fiveSeries.parkingAssist)
print (fiveSeries.make)
print (fiveSeries.model)
print (fiveSeries.year)"""
