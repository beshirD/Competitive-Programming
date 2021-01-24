def sortColors(nums):
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i] > nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                
    print(nums)
    
sortColors([2,0,2,1,2,1,0])