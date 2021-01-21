def binarySearch(arr,x):
    result = []
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low)//2
        if arr[mid] < x and arr[mid-1] > x:
            result.append(mid + 1)
            break
        if arr[mid] < x:
            high = mid - 1
        elif arr[mid] > x:
            low = mid + 1
        else:
            result.append(mid + 1)
            break
    return result
print(binarySearch([90,34,30,20,4,3,2,1,1],20))
            
