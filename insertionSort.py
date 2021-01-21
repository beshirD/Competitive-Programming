def insertionSort(arr):
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                
    return arr
print(insertionSort([3,6,1,2,9,7]))