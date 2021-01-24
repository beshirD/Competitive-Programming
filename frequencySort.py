def frequencySort(nums):
    dic = {}
    result = []
    for i in nums:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    sortedDic = sorted((value,key) for (key,value) in dic.items())
    j = 0
    while j < len(sortedDic):
        if j < len(sortedDic)-1 and sortedDic[j][0] == sortedDic[j+1][0] :
            temp = sortedDic[j]
            sortedDic[j] = sortedDic[j+1]
            sortedDic[j+1] = temp
            result += [sortedDic[j][1]] * sortedDic[j][0]
            j+=1
        else:
            result += [sortedDic[j][1]] * sortedDic[j][0]
            j+=1
        


    print(result)
frequencySort([5,1,1,1,1,2,2,2,3,4,4,4,6,6,6,6])