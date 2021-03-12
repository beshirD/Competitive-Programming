
def bagOfTokensScore(tokens, P):
    tokens = sorted(tokens)
    score = 0
    result = 0
    for token in tokens:
        print(token) 
        if token <= P:
            P -= token
            score += 1
            result += 1
            
        elif token > P:
            if score > 0:
                P += tokens.pop()
                score -= 1
            else:
                return result
    return result
print(bagOfTokensScore([100,200,300,400],300))
                    