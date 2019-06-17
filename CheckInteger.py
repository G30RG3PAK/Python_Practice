def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Input must be integers")
    return a+b


print(add_numbers('a', 20))

