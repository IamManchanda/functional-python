""" Python Functions """

def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    return total

nums = [1, 567, 818, 98, 89]
print( sum_all_values(*nums) )
