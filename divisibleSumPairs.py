def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(n):
            if (i < j) and ((ar[i] + ar[j]) % k == 0):
            
                count += 1
    print(count)
divisibleSumPairs(6,3,[1,3,2,6,1,2])