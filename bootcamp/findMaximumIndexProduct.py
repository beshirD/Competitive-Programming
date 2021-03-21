def solve(arr):
    left = [0] * len(arr)
    ans = 0
    
    # Calculating left index 
    stack = [(arr[0], 0)]
    for i in range(1, len(arr)):
        while stack and stack[-1][0] <= arr[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1][1] + 1
        stack.append((arr[i], i))
        
    # Calculating right index 
    stack = [(arr[-1], len(arr) - 1)]
    for i in range(len(arr) - 2, -1, -1):
        while stack and stack[-1][0] <= arr[i]:
            stack.pop()
        if stack:
            currRight = stack[-1][1] + 1
            # calculating maximum product
            ans = max(left[i] * currRight, ans)
        stack.append((arr[i], i))

    return ans
