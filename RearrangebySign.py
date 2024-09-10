'''
arrange the array elements by sign positive followed by negative

Observations:
1. The positive elements are at the even positions
2. The negative elements are at the odd positions in the answer

Time Complexity: O(n)
Space Complexity: O(n)
'''

def Rearrange(nums):
    ans = [0]*len(nums) 
    posIndex = 0
    negIndex = 1
    for i in range(len(nums)):
        if nums[i] > 0:
            ans[posIndex] = nums[i]
            posIndex += 2
        else:
            ans[negIndex] = nums[i]
            negIndex += 2
        
    return ans

nums = [3, 1, -2, -5, 2, -4]
print(Rearrange(nums))