def repeatedString(s,n):
    lenOfs = len(s)
    count = 0
    rem = n % lenOfs
    div = n/lenOfs
    if s == 'a':
        return n
    for a in s:
        if a == 'a':
            count += 1
    r = count * div 
    for i in range(rem):
        if s[i] == 'a':
            r+=1
    return r
print(repeatedString('aba',10))
