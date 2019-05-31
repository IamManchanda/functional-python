""" Python Functions """

def sum_all(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print( sum_all(1, 2, 3) )
print( sum_all(1, 2, 3, 4, 5, 6)  )
