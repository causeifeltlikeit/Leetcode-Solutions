mod = 10**9 + 7
    summ = 0
    bitShift = 0

    for i in range(1, n + 1):
        if (i & (i - 1)) == 0:
            bitShift += 1
        summ = (summ << bitShift | i) % mod
    return summ