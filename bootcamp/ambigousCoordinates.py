class Solution:
    def ambiguousCoordinates(self, S: str):
        S = S[1:len(S)-1]
        res = []
        for i in range(1,len(S)):
            first = self.helper(S[:i])
            second = self.helper(S[i:])
            for i in first:
                for j in second:
                    res.append(f'({i}, {j})')      
        return res
    def helper(self,S):
        result = []
        if len(S) > 1 and S[0] == '0' and S[-1] == '0':
            return result
        if S[0] == '0' and S[-1] != '0':
            result.append('.'.join([S[0],S[1:]]))
            return result
        if S[0] != '0' and S[-1] == '0':
            result.append(S)
            return result
        if len(S) == 1:
            result.append(S)
            return result
        if  S[0] != '0' and S[-1] != '0':
            result.append(S)
            for i in range(1,len(S)):
                res = '.'.join([S[:i],S[i:]])
                result.append(res)
            return result
            
            