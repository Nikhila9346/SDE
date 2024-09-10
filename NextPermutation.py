'''
#31 NEXT PERMUTATION - Find the next permutation of the given array (lexicographically greater than the given array)

Observation:
1. Understand how you'll search for a word in dictionary

Time Complexity: O(n)
Space Complexity: O(1)
'''

def NextPermutation(nums):
    ind = -1
    n = len(nums)
    #finding the breakpoint
    for i in range(n-2, -1, -1):
        if nums[i] < nums[i+1]:
            ind = i
            break
    if ind == -1:
        return nums.reverse()

    #finding the element that is greater than and closest to ind
    for i in range(n-1, ind, -1):
        if nums[i] > nums[ind]:
            nums[i], nums[ind] = nums[ind], nums[i]
            break
    
    nums[ind+1:] = reversed(nums[ind+1:])

    return nums

nums = [2, 1, 5, 4, 3, 0, 0]
nums = [3, 2, 1]
ans = NextPermutation(nums)
print(ans)