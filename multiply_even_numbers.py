""" Python Functions """

def multiply_even_numbers(numbers):
    total = 1
    for num in numbers:
        if not (num % 2):
            total = total * num
    return total

print( multiply_even_numbers([2,3,4,5,6]) )
