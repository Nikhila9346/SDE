#268 MISSING NUMBER

#! Approach 1
def MissingNumber(nums):
    n = len(nums)
    xor1 = 0
    xor2 = 0
    for i in range(n):
        xor1 = xor1 ^ nums[i]
        xor2 = xor2 ^ (i+1)
    return xor1 ^ xor2

#! Approach 2
def MissingNumber2(nums):
    n =len(nums)
    sum1 = n*(n+1)//2
    sum2 = 0
    for i in nums:
        sum2 += i
    mis = sum1 - sum2
    return mis

nums = [1, 0, 3]
nums = [9,6,4,2,3,5,7,0,1]
print(MissingNumber(nums))
print(MissingNumber2(nums))