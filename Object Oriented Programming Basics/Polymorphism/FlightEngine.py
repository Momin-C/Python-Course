class Flight:
    def __init__(self,engine):
        self.engine = engine
    def startEngine(self):
        self.engine.start()

class AirbusEngine:
    def start(self):
        print ("Starting Airbus engine")

class BoeingEngine:
    def start(self):
        print ("Starting Boeing engine")

AE = AirbusEngine()
BE = BoeingEngine()
f = Flight(BE)
f.startEngine()
