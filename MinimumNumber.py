#268 MISSING NUMBER

def MissingNumber(nums):
    n = len(nums)
    xor1 = 0
    xor2 = 0
    for i in range(n):
        xor1 = xor1 ^ nums[i]
        xor2 = xor2 ^ (i+1)
    return xor1 ^ xor2

nums = [1, 0, 3]
nums = [9,6,4,2,3,5,7,0,1]
print(MissingNumber(nums))