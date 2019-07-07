from functools import wraps
from time import time

def speed_test(test_fn):
    @wraps(test_fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = test_fn(*args, **kwargs)
        end_time = time()
        print(f"Executing {test_fn.__name__}")
        print(f"Time Elapsed: {end_time - start_time}")
        return result
    return wrapper

@speed_test
def sum_nums_gen(num_range):
    return sum(x for x in range(num_range))

@speed_test
def sum_nums_list(num_range):
    return sum([x for x in range(num_range)])

num_range = 100000000
print( f"Gen. Exp. Result: {sum_nums_gen(num_range)}\n" )
print( f"List Comp. Result: {sum_nums_list(num_range)}\n" )
