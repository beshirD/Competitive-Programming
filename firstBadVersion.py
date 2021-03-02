# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        result = 1
        while start <= end:
            middle = start + (end - start)//2
            if isBadVersion(middle):
                result = middle
                end = middle - 1
            else:
                start = middle + 1
    
        return result