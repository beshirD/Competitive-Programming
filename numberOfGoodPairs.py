def numberOfGoodPairs(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] == arr[j] and i < j:
                count += 1 
    return count           
print(numberOfGoodPairs([1,1,1,1]))