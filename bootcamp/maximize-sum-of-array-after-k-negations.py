class Solution:
    def largestSumAfterKNegations(self, A, K: int) -> int:
        
        for i in range(K):
            j = A.index(min(A))
            A[j] = -1 * A[j]
        return sum(A)
            
        