""" Python Functions """

def last_element(item):
    if item:
        return item[-1]
    return None

print( last_element([1,2,3]) )
print( last_element([]) )
