""" Python Functions """

def ensure_correct_info(*args):
    if "Colt" in args and "Steele" in args:
        return "Welcome back Colt Steele!"
    if "Harry" in args and "Manchanda" in args:
        return "Welcome back Harry Manchanda!"
    return "Not sure who you are..."

print( ensure_correct_info() )
print( ensure_correct_info(1, True, "Steele", "Colt") )
print( ensure_correct_info(1, True, "Manchanda", "Harry") )

