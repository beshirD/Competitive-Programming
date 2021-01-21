def relativeSortArray(arr1,arr2):
    dic = {}
    result = []
    for n in arr1:
        if n in dic:
            dic[n] += 1
        else:
            dic[n] = 1
    for k in arr2:       
        for i in range(dic[k]):
            result.append(k)
    for i in sorted(dic.keys()):
        if i in arr2:
            continue
        else:
            for j in range(dic[i]):
                result.append(i)
    return result
print(relativeSortArray([2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31],[2,42,38,0,43,21]))
