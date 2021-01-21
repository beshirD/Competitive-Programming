def pancakeSort(arr):
    result = []
    size = len(arr)
    for i in range(size, 1, -1):
        n = arr.index(i)
        arr = arr[-1:n:-1] + arr[:n]
        result += [n+1, i]
    return result

print(pancakeSort([3,2,4,1]))