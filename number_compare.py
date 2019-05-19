""" Python Functions """

def number_compare(a, b):
    if a > b:
        return "First is greater"
    if b > a:
        return "Second is greater"
    return "Numbers are equal"

print( number_compare(1, 1) )
print( number_compare(1, 0) )
print( number_compare(2, 4) )
