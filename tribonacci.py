def tribonacci(n):
    j = 0
    k = 1
    m = 1
    summ = 0
    if n == 0 or n == 1:
        return n
    elif n == 2:
        return 1
    else:
        for i in range(2,n):
            summ = j + k + m
            j = k
            k = m
            m = summ
        return summ
print(tribonacci(25))