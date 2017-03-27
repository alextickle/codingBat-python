def last2(str):
    if len(str) < 4:
        return 0
    sub = str[-2:]
    count = 0
    for i in range(len(str) - 1):
        if str[i] + str[i + 1] == sub:
            count = count + 1
    if count != 0:
        return count - 1
        