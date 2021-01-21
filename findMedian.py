def findMedian(arr):
    sortedArray = sorted(arr)
    mid = len(sortedArray)//2
    median = sortedArray[mid]
    return median
print(findMedian([0 ,1 ,2 ,4 ,6 ,5 ,3]))