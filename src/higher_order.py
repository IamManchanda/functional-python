def sum(num, my_function):
	total = 0;
	for n in range(1, num + 1):
		total += my_function(n)
	return total

def square(x):
	return x ** 2

def cube(x):
    return x ** 3

print( sum(10, square) )
print( sum(10, cube) )
