def palindromePer(r):
    dic ={}
    for i in r:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    oddCount = 0
    for j in dic:
        if dic[j] % 2 != 0:
            oddCount += 1
    return oddCount < 2
print(palindromePer("tactcoa")) 