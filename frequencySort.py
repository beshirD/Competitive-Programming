class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:   
        arr = []
        result = []
        for i in range(101):
            arr.append([])
    
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for key , values in dic.items():
            
            arr[values].append(key)
        for j in range(len(arr)):
            if len(arr[j]) > 0:
                arr[j] = sorted(arr[j],reverse=True)
                for k in range(len(arr[j])):
                    for m in range(j):
                        result.append(arr[j][k])
        return result

        