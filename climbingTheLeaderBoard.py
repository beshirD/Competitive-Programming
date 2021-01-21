def climbingLeaderBoard(ranked,player):
    scores = sorted(list(set(ranked)), reverse=True)
    result = []
    for n in player:
        while len(scores) != 0 and n >= scores[-1]:
            scores.pop()
        result.append(len(scores) + 1)
    return result
print(climbingLeaderBoard([100, 100 ,50 ,40 ,40,20,10],[5,25,50,120]))
