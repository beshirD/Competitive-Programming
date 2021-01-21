def bonAppetit(bill,k,b):
    totalSum = 0
    totalShared = 0
    actualCharge = 0
    for n in bill:
        totalSum += n
    actualShared = totalSum - bill[k]
    actualCharge = totalShared / 2
    if actualCharge == b:
        print("Bon Appetit")
    else:
        print(b - actualCharge)

