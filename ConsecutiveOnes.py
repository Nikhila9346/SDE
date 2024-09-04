#485 MAX CONSECUTIVE ONES

def maxConsecutive(nums):
    n = len(nums)
    count = 0
    maxi = 0
    for i in nums:
        if i!= 1:
            count = 0
        else:
            count += 1
            if count > maxi:
                maxi = count
    return maxi

nums = [1, 1, 0, 1, 1, 1, 0, 1, 1]
print(maxConsecutive(nums))