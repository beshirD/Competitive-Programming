def removeDuplicates(self, S: str) -> str:
    i = 1
    while i < len(S):
        letter = S[i]
        if S[i-1] == letter:
            i = 0
            letter *= 2
            S = S.replace(letter,"")
        i += 1
    return S
            