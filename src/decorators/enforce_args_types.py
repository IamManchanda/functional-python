def enforce_args_types(*types):
    def decorator(fn):
        def new_func(*args, **kwargs):
            new_args = []
            for (a, t) in zip(args, types):
                new_args.append( t(a) )
            return fn(*new_args, **kwargs)
        return new_func
    return decorator

@enforce_args_types(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)

repeat_msg("Hello", "3")
