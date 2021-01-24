def quickSort(arr):
    left = []
    right = []
    equal = []
    for i in arr:
        if i < arr[0]:
            left.append(i)
        elif i > arr[0]:
            right.append(i)
        else:
            equal.append(i)
    result = left + equal + right
    for j in result:
        print(j,end=" ")
