def balancedSums(arr):
    left = 0
    right = sum(arr)
    for num in arr:
        if (right - num) == left:
            return "YES"
        else:
            left += num
            right -= num
    return "NO"