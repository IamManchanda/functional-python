import sys
# A simple comparison of size (in Bytes)
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

print("To do the same thing, it takes...")
print(f"List Comprehension: {list_comp} bytes")
print(f"Generator Expression: {gen_exp} bytes")

""" 
So, the conclusion is that we should be using gen_exp instead of list comprehensions wherever possible

nums = [2, 60, 20, 21]

# Don't do this
all([num % 2 == 0 for num in nums])
any([num % 2 == 0 for num in nums])

# Do this
all(num % 2 == 0 for num in nums)
any(num % 2 == 0 for num in nums)
"""
