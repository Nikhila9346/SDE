def SingleNumber(nums):
    hashMap = {}
    for i in nums:
        if i not in hashMap:
            hashMap[i] = 1
        else:
            hashMap[i] += 1
    for key in hashMap:
        if hashMap[key] == 1:
            return key

nums = [4,1,2,1,2]
print(SingleNumber(nums))