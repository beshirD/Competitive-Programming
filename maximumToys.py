def maximumToys(prices,k):
    sortedPrices = sorted(prices)
    maximumSum = 0
    count = 0
    for i in sortedPrices:
        maximumSum += i
        if maximumSum < k:
            count+=1
    return count
print(maximumToys([1 ,12, 5 ,111 ,200 ,1000 ,10],50))