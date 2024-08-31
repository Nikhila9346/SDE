def InsertionSort(arr, n):
    for i in range(1, n):
        j = i
        while(j > 0 and arr[j-1]>arr[j]):
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr
arr = [20, 5, 40, 60, 10, 30]
print(InsertionSort(arr, len(arr)))

#[5, 10, 20, 40, 60, 30]

#[5, 10, 20, 30, 40, 60 ]

'''
Time Complexity: O(n^2)
Space Complexity: O(1)
'''

#find the no.of pairs which adds up to given sum