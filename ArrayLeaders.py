'''

'''

def arrayLeaders(n, nums):
    maxi = 0
    l = []
    i = 1
    while i < n:
        if nums[maxi] > nums[i]:
            l.append(nums[maxi])
            i += 1
            if nums[i] > nums[i+1]:
                i += 1
            else:
                maxi = i + 1
                i += 2
        else:
            maxi = i
            i += 1
    l.append(nums[n-1])
    return l

nums = [16,17,4,3,5,2]
print(arrayLeaders(len(nums), nums))