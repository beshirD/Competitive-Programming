def isAnagram(s,t): 

    dic = {}
    for i in s:
        if i in dic:
            dic[i] +=1 
        else:
            dic[i] = 1
    for j in t:
        if j in dic:
            dic[j] -=1
        else:
            return False
    for k in dic:
        if dic[k] != 0:
            return False
    return True

print(isAnagram("video game","give a demo"))
