def reverse(self, x: int) -> int:
    numString = str(abs(x))
    numString = numString.strip()
    numString = numString[::-1]
    num = int(numString)
    if num >= 2**31 - 1 or num <= -2** 31:
        return 0
    elif x < 0:
        return num * -1
    else:
        return num
