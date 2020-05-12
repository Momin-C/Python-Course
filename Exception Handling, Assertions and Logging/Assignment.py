try:
    password = input("Input password: ")
    assert len(password)>=8, "Password is too short"
except AssertionError as obj:
    print (obj)
