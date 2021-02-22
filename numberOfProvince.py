class Solution:
    def findCircleNum(self, isConnected):
        numberOfProvince = 0
        isVisited = set()
        for i in range(len(isConnected)):
            if i not in isVisited:
                numberOfProvince += 1
                self.dfs(isConnected,i,isVisited)
        return numberOfProvince
    def dfs(self,isConnected,i,isVisited):
        for j in range(len(isConnected[i])):
            if isConnected[i][j] and j not in isVisited:
                isVisited.add(j)
                self.dfs(isConnected,j,isVisited)