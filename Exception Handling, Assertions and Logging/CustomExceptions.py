class OverTheLimitException(Exception):
    def __init__(self,msg):
        msg = self.msg

def withdrawal(amount):
    if amount>500:
        raise OverTheLimitException("You cannot withdraw that much")

withdrawal(500)
