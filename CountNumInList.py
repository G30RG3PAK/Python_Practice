def list_count(innum):
    count = 0
    for num in innum:
        if num == 4:
            count = count + 1

    return count


print(list_count([1, 4, 6, 7, 4]))
print(list_count([1, 4, 6, 4, 7, 4]))

