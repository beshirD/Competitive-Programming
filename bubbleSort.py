
def bubbleSort(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range((len(arr) - 1)):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
                swapped = True
                
    print(arr)
    
bubbleSort([3,1,2,7,1,10,1])