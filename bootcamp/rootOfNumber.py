
def root(x, n):
    
    start = 0
    middle = 0
    if x < 1:
        end = 1
    else:
        end = x
    while (end - start) >= 0.001:
        result = 1
        middle = start + (end - start)/2
        for i in range(n):
            result *= middle
        if result > x:
            end = middle
        elif result < x:
            start = middle
        else:
            break
    return middle
print(root(7,3))
  

