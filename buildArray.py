def buildArray(self, target: List[int], n: int) -> List[str]:
    arr = []
    result = []
    for i in range(1,target[-1]+1):
        arr.append(i)
        result.append("Push")
        if i not in target:
            arr.pop()
            result.append("Pop")
    return result