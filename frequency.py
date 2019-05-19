""" Python Functions """

def frequency(collection, searchTerm):
    return collection.count(searchTerm)

print( frequency([1, 2, 3, 4, 4, 4], 4) )
print( frequency([True, False, True, True], False) )
