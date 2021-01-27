def isValid(s):
    opening = ['(','{','[']
    ending = [')','}',']']
    result = []
    for i in s:
        if i in opening:
            result.append(i)
        elif i in ending:
            if len(result) == 0:
                return False
            elif i == ')':
                if result[-1] == '(':
                    result.pop()
                else:
                    return False
            elif i == '}':
                if result[-1] == '{':
                    result.pop()
                        
                else:
                    return False
            elif i == ']':
                if result[-1] == '[':
                    result.pop()
                else:
                    return False
            
    return len(result) == 0
print(isValid("({()([][])})"))