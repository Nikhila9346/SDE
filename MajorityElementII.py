def MajorityElementII(nums):
    n = len(nums)
    ele1, ele2 = float('-inf'), float('-inf')
    count1 = 0
    count2 = 0

    for i in nums:
        if count1 == 0 and i != ele2:
            ele1 = i
            count1 = 1
        elif count2 == 0 and i != ele1:
            ele2 = i
            count2 = 1
        elif ele1 == i:
            count1 += 1
        elif ele2 == i:
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1
    return ele1, ele2

nums = [1, 1, 1, 2, 2, 3, 3, 3]
print(MajorityElementII(nums))