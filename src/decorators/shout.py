def shout(shout_fn):
    def wrapper(*args, **kwargs):
        return shout_fn(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi, I'm {name}."

@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please."

@shout
def lol():
    return "Lol!!!"

print( greet("Harry Manchanda") )
print( order("Burger", "Fries") )
print( lol() )
