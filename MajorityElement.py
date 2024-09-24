'''
Majority Element n/2 (The array contains exactly one majority Element)

Time Complexity: O(n)
Space Complexity: O(1)
'''

def MajorityElement(nums):
    count = 0
    ele = 0
    for i in nums:
        if count == 0:
            ele = i
        count += 1 if i == ele else -1
    return ele

nums = [3, 1, 1]
print(MajorityElement(nums))