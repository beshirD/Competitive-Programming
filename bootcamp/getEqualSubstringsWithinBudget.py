class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # max_length = 0
        # for i in range(len(s)):
        #     curr_length = 0
        #     cost = 0
        #     while cost <= maxCost and i < len(s):
        #         cost += abs(ord(s[i]) - ord(t[i]))       
        #         if cost <= maxCost:
        #             curr_length += 1
        #         i += 1
        #     max_length = max(max_length,curr_length)
        # return max_length
        start = 0
        sec = 0
        cost = 0
        count = 0
        max_count = 0
        while sec < len(s):
            cost += abs(ord(s[sec]) - ord(t[sec]))
            if cost <= maxCost:
                sec += 1
                count += 1
            else:
                cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
                sec += 1  
            max_count = max(max_count, sec - start)
        return max_count
                