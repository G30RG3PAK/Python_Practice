def FuncResult(n):
    return lambda a: a * n


ReturnResult = FuncResult(15)


print(ReturnResult(20))




