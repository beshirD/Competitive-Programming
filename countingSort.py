def countingSort(arr):
    m = max(arr) + 1
    result = []
    temp = [0] * m
    for n in arr:
        temp[n] += 1
    
    for i in range(len(temp)):
        for j in range(temp[i]):    
            result.append(i)
    return result
print(countingSort([2,7,1,2,4,2,5]))