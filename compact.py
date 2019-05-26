""" Python Functions """

def compact(my_list):
    return [val for val in my_list if val]

print( compact([0,1,2,"",[], False, {}, None, "All done"]) )
