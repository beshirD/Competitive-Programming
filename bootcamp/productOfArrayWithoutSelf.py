class Solution:
    def productExceptSelf(self, nums):
        product = [1]
        revproduct = [1]
        answer = []
        start = 1
        start1 = 1
        for i in nums:
            start *= i
            product.append(start)
        nums.reverse()
        for i in nums:
            start1 *= i
            revproduct.append(start1)
        for i in range(1,len(product)):
            answer.append(product[i-1] * revproduct[len(product) - 1- i] )
        return answer