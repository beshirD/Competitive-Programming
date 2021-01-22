def digitSum(n,k):
    n = str(n) * k
    m = int(n)
    summ = 0
    if m < 10:
        return n
    while m >= 1:
        summ += m%10
        m = m//10
    return(digitSum(summ,1))
print(digitSum(123,3))