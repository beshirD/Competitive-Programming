class Solution:
    def minIncrementForUnique(self, A) -> int:
        A = sorted(A)
        i = 0
        j =  1
        count = 0
        while j < len(A):
            if A[i] == A[j]:
                A[j] += 1
                count += 1
            elif A[i] > A[j]:
                diff = A[i] - A[j]
                A[j] += diff + 1
                count += diff + 1
            i += 1
            j += 1
         
        return count
            
       
        
                 
        