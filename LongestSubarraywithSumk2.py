'''
Works only for positive integers (not solved)
'''

def LongestSubarray(nums, k):
    sum1 = 0
    maxi = 0
    i = 0
    j = 0
    while (j < len(nums)):
        sum1 += nums[j]
        if sum1 == k:
            maxi = max(maxi, j - i + 1)
        elif sum1 < k:
            pass
        else:
            sum1 -= nums[i]
            i += 1
        j += 1
    return maxi


nums = [1, 2, 3, 1, 1, 1, 1, 3, 3]
k = 6
print(LongestSubarray(nums, k))