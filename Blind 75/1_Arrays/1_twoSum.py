'''
Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 14
Result: YES (for 1st variant)
       [1, 3] (for 2nd variant)
Explanation: arr[1] + arr[3] = 14. So, the answer is “YES” for the first variant and [1, 3] for 2nd variant.

Input Format: N = 5, arr[] = {2,6,5,8,11}, target = 15
Result: NO (for 1st variant)
	[-1, -1] (for 2nd variant)
Explanation: There exist no such two numbers whose sum is equal to the target.

'''

#! COMBO OF FIRST VARIANT
def twoSum(arr, k, n):
    l = 0
    r = n-1
    arr = arr.sort()
    while l <= r:
        sum = arr[l] + arr[r]
        if sum > k:
            r -= 1
        elif sum < k:
            l += 1
        else:
            return "YES"
        
    return "No"

arr = [2,6,5,8,11]
# print(twoSum(arr, 14, len(arr)))
print(twoSum(arr, 15, len(arr)))         #No



#? THINK OF IT IN THE CASE OF UNSORTED ARRAY AND 2nd VARIANT (USING HASHMAP)

def twoSum2(arr, target, n):
    hashMap = {}        #val : index

    for i, n in enumerate(arr):
        diff = target - n
        if diff in hashMap:
            return [i, hashMap[diff]]
        hashMap[n] = i

arr = [3,2,4]
print(twoSum2(arr, 6, len(arr)))          #[2, 1]

