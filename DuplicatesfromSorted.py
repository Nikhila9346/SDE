#26 REMOVE DUPICATES FROM THE SORTED ARRAY

def removeDuplicates(nums):
    i = 0
    j = 1
    count = 1
    while j <= len(nums)-1:
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
            count += 1
        j += 1
    return count, nums


nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))