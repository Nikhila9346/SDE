def MoveZeros(nums):
    l = 0
    for r in range(len(nums)):
        if nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
    return nums


nums = [1, 0, 3, 0, 12]
print(MoveZeros(nums))       #[1, 3, 12, 0, 0]