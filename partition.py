""" Python Functions """

def isEven(num):
    return num % 2 == 0

def partition(my_list, fn):
    return [
        [val for val in my_list if fn(val)], 
        [val for val in my_list if not fn(val)],
    ]

print( partition([1,2,3,4], isEven) )
