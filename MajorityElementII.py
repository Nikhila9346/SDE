def MajorityElementII(nums):
    n = len(nums)
    ele1, ele2 = float('-inf'), float('-inf')
    count1 = 0
    count2 = 0
    l= []

    for i in nums:
        #finding the elements who appear more times in array
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
    #finding how many time ele1, ele2 appears

    count1, count2 = 0, 0
    for i in nums:
        if i == ele1:
            count1 += 1
        if i == ele2:
            count2 += 1
    
    #check whether ele1, ele2 appears more than n/3 times
    if count1 > n//3:
        l.append(ele1)
    if count2 > n//3:
        l.append(ele2)
    return l
    
nums = [1, 1, 1, 2, 2, 3, 3, 3]
# nums = [3, 2, 3]
nums = [2, 2]
print(MajorityElementII(nums))