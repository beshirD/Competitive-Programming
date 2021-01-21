def sockMerchant(n, ar):
    dic = {}
    pairCount = 0
    for numbers in ar:
        if numbers in dic:
            dic[numbers] += 1
        else:
            dic[numbers] = 1

     
    for val in dic:
        pairCount += math.floor(dic[val]/2)
    return pairCount