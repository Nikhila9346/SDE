#238
'''
Given an array nums, return an array answer such that answer[i] is equal to the product of the nums except nums[i]
'''


def productofArray(nums):
    answer = [1] * len(nums)
    prefix =1
    for i in range(len(nums)):
        answer[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        answer[i] *= postfix
        postfix *= nums[i]
    return answer

nums = [1,2,3,4]
nums =[-1,1,0,-3,3]
print(productofArray(nums))

#o/p
# [0, 0, 9, 0, 0]