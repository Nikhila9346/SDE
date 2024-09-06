def LongestSubarray(nums, k):
    maxi = 0
    sum1 = 0
    length = 0
    hashMap = {}
    for i in range(len(nums)):
        sum1 += nums[i]
        diff = sum1 - k
        if diff in hashMap:
            length = i - hashMap[diff]
            if length > maxi:
                maxi = length
        if sum1 == k:
            length = i+1
        if sum1 not in hashMap:
            hashMap[sum1] = i 

    return maxi, hashMap

nums = [10, 5, 2, 7, 1, 9]
k = 15
nums = [2, 0, 0, 3]
print(LongestSubarray(nums, k))