def countingValleys(steps, path):
    numOfValleys = 0
    count = 0
    for step in path:
        if step == 'U':
            count += 1
        if step == 'D':
            count-=1
        if count == 0 and step == 'U':
            numOfValleys += 1
    return numOfValleys
# print(countingValleys(8,'UDDDUDUU'))