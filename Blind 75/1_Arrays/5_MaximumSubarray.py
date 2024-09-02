def maxSubarraySum(arr):
    max_sum = arr[0]
    cur_sum = 0
    for i in arr:
        #if sum less than zero make sum = 0
        if cur_sum < arr[i]:
            cur_sum = arr[i]
        #update the sum by adding i value
        cur_sum += i
        if cur_sum > max_sum:
            max_sum = cur_sum
    return max_sum


arr = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubarraySum(arr))    #6