def proeuler():
    res = sum(x for x in range(1000) if(x % 3 == 0 or x % 5 == 0))
    return str(res)


if __name__ == "__main__":
    print(proeuler())

