def secondLargest(nums):
    slargest = -1
    largest = nums[0]
    for i in range(len(nums)):
        if nums[i] > largest:
            slargest = largest
            largest = nums[i]
        elif (nums[i] < largest and nums[i] > slargest):
            slargest = nums[i]
    return slargest

def secondSmallest(nums):
    ssmallest = float('inf')
    smallest = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < smallest:
            ssmallest = smallest
            smallest = nums[i]
        elif nums[i] > smallest and nums[i] < ssmallest:
            ssmallest =nums[i]
    return ssmallest


# arr = [12, 35, 1, 10, 34, 1]
arr = [10, 10, 10]
print(secondLargest(arr))
print(secondSmallest(arr))