class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        s = list(s)
        stack = []
        count = 1
        i = 0
        while i < len(s): 
            if len(stack) == 0:
                stack.append([s[i],1])
            elif stack[-1][0] != s[i]:
                stack.append([s[i],1])
            elif stack[-1][0] == s[i]:
                stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
            i += 1
        result = []
        for letter in stack:
            result.append(letter[0] * letter[1])
        return "".join(result)
        