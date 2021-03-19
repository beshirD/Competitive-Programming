class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
#         if len(s) == 0 or len(s) == 1:
#             return len(s)
#         i = 0
#         j = 0
#         max_length = 0
#         visited = dict()
#         while j < len(s):
#             if s[j] not in visited:
#                 visited[s[j]] = j
#                 j += 1
#                 max_length = max(max_length,(j-i))
#             else:
#                 max_length = max(max_length,(j-i))
#                 i = visited[s[j]] + 1
#                 visited[s[j]] = j
#                 j += 1
            
#         return max_length 
        s = list(s)
       
        i = 0
        j = 0
        count = 0
        visited = set()
        max_count = 0
        while j < len(s):
            if s[j] not in visited:
                visited.add(s[j])
                max_count = max(max_count , j - i + 1)
            else:   
                while (s[j] in visited):
                    # print(visited,s[j])
                    visited.remove(s[i])
                    # print(visited)
                    i += 1
                visited.add(s[j])
            j += 1       
        return max_count
                    