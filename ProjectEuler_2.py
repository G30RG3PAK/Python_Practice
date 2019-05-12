def evenfibo():
    result = 0
    x = 1
    y = 2
    while x <= 100:
        if x % 2 == 0:
            result += x
        x, y = y, x + y
    return str(result)


if __name__ == "__main__":
    print(evenfibo())


