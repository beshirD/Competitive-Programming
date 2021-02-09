
def dailyTemperatures(self, T: List[int]) -> List[int]:
    result = []
    for i in range(len(T) - 1):
        if T[i] < T[i+1]:
            result.append(1)
            # print(i)
            # print(result)
            # print(T)
        else:
            D = T[i] - T[i+1]
            if D >= len(T) - i:
                result.append(0)
            else:
                result.append(D)
            # print(i)
            # print(result)
            # print(T)
    result.append(0)
    return result