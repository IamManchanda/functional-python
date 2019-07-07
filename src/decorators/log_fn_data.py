from functools import wraps

def log_fn_data(log_fn):
    @wraps(log_fn)
    def wrapper(*args, **kwargs):
        print(f"You are about to call: {log_fn.__name__}")
        print(f"Here's the documentation:\n =>{log_fn.__doc__}\n")
        return log_fn(*args, **kwargs)
    return wrapper

@log_fn_data
def add(x, y):
    """ Add two numbers together """
    return x + y

print( add.__doc__ )
print( add.__name__ )
help(add)
