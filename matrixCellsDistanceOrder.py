
def matrixCellsDistanceOrder(R,C,r0,c0):
    M = []
    for i in range(R):
        for j in range(C):
            M.append([i,j])
    for i in range(R):
        for j in range(C):
            M[i][j] = abs(r0-i) + abs(c0-j)
    print(M)
matrixCellsDistanceOrder(2,2,0,1)