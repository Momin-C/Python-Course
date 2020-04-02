def hello(name):
    def wrapper():
        return "Hello" + name
    return wrapper()

def howareyou():
    return "How are you"

howareyou = hello(howareyou)
howareyou("Momin")
