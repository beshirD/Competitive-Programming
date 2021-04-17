"""
1. initialize left array 
2. initialize stack with (arr[0] , 0)
3. iterate over arr
    3.1 while stack not empty and top of stack is <= current num
        3.1.1 pop from stack
    3.2 if stack 
        3.2.2 left[i] = stack[-1][1] + 1
    3.3 stack.append(arr[i],i)
"""

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
