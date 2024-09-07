def subarraySum(nums, k):
    preSum = 0
    res = 0
    hashMap = {0 : 1}

    for i in nums:
        preSum += i
        dif = preSum - k
        if dif in hashMap:
            hashMap[dif] += 1
            res += hashMap[dif]
        if preSum not in hashMap:
            hashMap[preSum] = 1
        else:
            hashMap[preSum] += 1
    return res

nums = [1, -1, 1, 1, 1, 1]
print(subarraySum(nums, 3))