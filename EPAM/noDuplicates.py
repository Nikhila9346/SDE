'''
Return the string without duplicates (case-insensitive) and the order should be preserved
'''

def case(k):
    l = ord(k) + 32 if 65<=ord(k)<=90 else ord(k) - 32
    # if 65<=ord(k)<=90:
    #     l = ord(k) + 32
    # else:
    #     l = ord(k) - 32
    return chr(l)

def noDuplicates(nums):
    i = 0
    s = nums[0]
    for j in range(1, len(nums)):
        dif = ord(nums[i]) - ord(nums[j])
        if dif not in [32, -32, 0]:
            if (nums[j] not in s) and (case(nums[j]) not in s):
                s += nums[j]
                i = j
    return s

nums = "AaaBbbCDE"
nums = "aAbBcde"
nums = "ababa"
nums = "abABa"  
print(noDuplicates(nums))