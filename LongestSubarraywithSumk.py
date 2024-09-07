'''
Works for positive integers, negatives and zeros
This is an optimal solution for any values
'''

def LongestSubarray(nums, k):
    maxi = 0
    sum1 = 0
    length = 0
    count = 0
    hashMap = {0:-1}    #if you're getting the sum = 0 somewhere in the middle that means even if you add the values before it doesn't affect it which results in the longest length of the subarray

    for i in range(len(nums)):
        sum1 += nums[i]
        if sum1 not in hashMap:
            hashMap[sum1] = i 
        diff = sum1 - k
        if diff in hashMap:
            length = i - hashMap[diff]
            count += 1
        if length > maxi:
            maxi = length

    return maxi, hashMap, count

nums = [10, 5, 2, 7, 1, 9]
k = 15
# nums = [2, 0, 0, 3]
# k = 3
# nums =[-7, 17, -12, 2, 11, -1, 4, 11, -18]
# k = 25
print(LongestSubarray(nums, k))