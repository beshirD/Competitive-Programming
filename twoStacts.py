def twoStacks(x,a,b):
    possibleLists = []
    possibleSum = 0
    count = 0
    for i in range(len(a)):
        if possibleSum + a[0] <= x:
            possibleSum += a[0]
            count += 1
            possibleLists.append(a[0])
            a.pop(0)
    maxAmoves = count
    for j in range(len(b)):
        possibleSum += b[0]
        b.pop(0)
        count += 1
        while possibleSum > x and count > 0 and len(possibleLists) > 0:
            count -= 1
            possibleSum -= possibleLists[-1]
            possibleLists.pop()
        if possibleSum <= x and count > maxAmoves:
            maxAmoves = count
    return maxAmoves
print(twoStacks(20,[10,9,8,2,8],[16,1,1,1,1,0,8]))
