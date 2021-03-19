def gridlandMetro(n, m, k, track):
    visited = {}
    count = 0
    for i in range(k):
        tr = track[i]
        if tr[0] not in visited: 
            visited[tr[0]] = (tr[1],tr[2])
            count += (tr[2] - tr[1])+1
        else:
            prev = visited[tr[0]]
            if tr[1] > prev[1] or tr[2] < prev[0]:
                count += (tr[2] - tr[1])+1
            else:   
                if tr[1] < prev[0]:
                    count += (prev[0]-tr[1])
                    visited[tr[0]] = (tr[1],prev[1]) 
                if tr[2] > prev[1]:
                    count += (tr[2]-prev[1])
                    visited[tr[0]] = (prev[0],tr[2])           
    return (n*m) - count
