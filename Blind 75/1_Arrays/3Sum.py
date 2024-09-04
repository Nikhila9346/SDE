def ThreeSum(nums):
    nums = sorted(nums)
    n = len(nums)
    l = []
    for i in range(n):
        j = i + 1
        k = n - 1
        if i>0 and nums[i] == nums[i-1]:
            continue
        while j<k:
            sum1 = nums[i] + nums[j] + nums[k]
            if sum1 < 0:
                j += 1
            elif sum1 > 0:
                k -= 1
            else:
                l.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j<k and nums[j] == nums[j-1]:
                    j += 1
                while j<k and nums[k] == nums[k+1]:
                    k -= 1
    return l

nums = [-1,0,1,2,-1,-4]
print(ThreeSum(nums))