""" Python Functions """

def speak(animal = "dog"):
    noises = {
        "pig": "oink", 
        "duck": "quack", 
        "cat": "meow", 
        "dog": "woof"
    }
    return noises.get(animal, "?")

print( speak() )
print( speak("pig") )
print( speak("duck") )
print( speak("cat") )
print( speak("dog") )
print( speak("daww") )
