def noDuplicates(nums):
    i = 0
    s = nums[0]
    for j in range(1, len(nums)):
        dif = ord(nums[i]) - ord(nums[j])
        if dif not in [32, -32, 0]:
            if (nums[j].upper() not in s) and (nums[j].lower() not in s):
                s += nums[j]
                i = j
    return s

nums = "AaaBbbCDE"
nums = "aAbBcde"
nums = "ababa"
nums = "abABa"  
print(noDuplicates(nums))