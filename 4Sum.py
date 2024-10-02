'''
Return all the subarrays that sum to k
Time Complexity: O(n2)
Space Complexity: O(n)
'''

def FourSum(arr, n, target):
    v = []
    arr = sorted(arr)
    for i in range(n-3):
        if i>0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1, n-2):
            if j > i+1 and arr[j] == arr[j-1]:
                continue 
            k = j + 1
            l = n - 1
            while k<l:
                sum1 = arr[i] + arr[j] + arr[k] + arr[l]
                if sum1 > target:
                    l -= 1
                elif sum1 < target:
                    k += 1
                else:
                    v.append([arr[i], arr[j], arr[k], arr[l]])
                    while k < l and arr[k] == arr[k+1]:
                        k += 1
                    while l > k and arr[l] == arr[l-1]:
                        l -= 1
                    k += 1
                    l -= 1
    return v

arr = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5]
# arr = [1, 0, -1, 0, -2, 2]
n = len(arr)
k=8
# k = 0
print(FourSum(arr, n, k))