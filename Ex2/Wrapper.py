def f1(func):
    # Wrapper function
    def wrapper(*args, **kwargs):
        print("Started")
        val = func(*args, **kwargs)
        print("Ended")
        return val

    return wrapper


# Using decorators
@f1
def f(a, b=9):
    print(a, b)


@f1
def add(x, y):
    return x + y


print(add(4, 5))
