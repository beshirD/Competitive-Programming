def sortColors(nums):
    left = 0
    right = len(nums)-1
    i = 0
    while i <= right:
        if nums[i] == 0:
            nums[left] = nums[i]
            i += 1
            left += 1
            print(nums)
        elif nums[i] == 2:
            temp = nums[i]
            nums[i] = nums[right]
            nums[right] = temp
            right -= 1
            i+=1
            print(nums)
        else:
            i += 1
            print(nums)
    print(nums)
    
sortColors([2,0,2,1,2,1,0])