from abc import abstractmethod,ABC
class TouchScreenLaptop(ABC):
    @abstractmethod
    def scroll(self):
        pass
    @abstractmethod
    def click(self):
        pass

class HP(TouchScreenLaptop):
    def scroll(self):
        print ("HP Scrolling")

class Dell(TouchScreenLaptop):
    def scroll(self):
        print ("Dell Scrolling")

class HPNotebook(HP):
    def click(self):
        print ("HP Notebook Clicking")

class DellNotebook(Dell):
    def click(self):
        print ("Dell Notebook Clicking")

h = HPNotebook()
h.scroll()
h.click()

d = HPNotebook()
d.scroll()
d.click()
