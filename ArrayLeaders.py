'''
Input: arr = [4, 7, 1, 0]
Output: 7 1 0
Explanation: Rightmost element is always a leader. 7 and 1 are greater than the elements in their right side.

Time Complexity: O(n)
Space Complexity: O(n)
'''

def arrayLeaders(n, nums):
    maxi = float('-inf')
    l = []

    for i in range(n-1, -1, -1):
        if nums[i] > maxi:
            l.append(nums[i])
            maxi = nums[i]
    return l[::-1]

nums = [16,17,4,3,5,2]
print(arrayLeaders(len(nums), nums))