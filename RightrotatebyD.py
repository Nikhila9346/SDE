def RightRotate(nums, d):
    reverse(nums, 0, len(nums)-d-1)
    reverse(nums, len(nums)-d, len(nums)-1)
    reverse(nums, 0, len(nums)-1)
    return nums

def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

nums = [1, 2, 3, 4, 5, 6, 7] 
print(RightRotate(nums, 3))      #[5, 6, 7, 1, 2, 3, 4]
# print(nums)