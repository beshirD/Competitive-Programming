def intersection(nums1,nums2):
        num1 = list(set(nums1))
        num2 = list(set(nums2))
        result = []
        for n in num1:
            if n in num2:
                result.append(n)
        return result
print(intersection([4,9,5],[9,4,9,8,4]))