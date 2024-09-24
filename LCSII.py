def Longest(nums):
    hashMap = {}
    count = 1
    maxi_len = 0

    for i in nums:
        if i not in hashMap:
            hashMap[i] = 1
        else:
            hashMap[i] += 1
    
    for i in hashMap:
        if i-1 not in hashMap:
            count = hashMap[i]
            start = i
            while start + 1 in hashMap:
                count += hashMap[start+1]
                start += 1
            if count > maxi_len:
                maxi_len = count
    return maxi_len

nums = [5, 8, 3, 2, 1, 1, 4]
nums = [102, 4, 100, 1, 101, 3, 2, 1, 1, 2]
nums = [0,3,7,2,5,8,4,6,0,1]
print(Longest(nums))