def be_polite(polite_fn):
    def wrapper():
        print("What a pleasure to meet you")
        polite_fn()
        print("Have a Great Day!")
    
    return wrapper

@be_polite
def greet():
    print("My Name is Matt")

greet()
