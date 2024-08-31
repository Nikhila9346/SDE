def BubbleSort(arr, n):
    for i in range(n-1):        #for n elements we do (n-1) passes
        flag = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if flag == False:
            break
    return arr

arr = [4, 1, 3, 9, 7]
print(BubbleSort(arr, len(arr)))

#[1, 3, 4, 7, 9]


'''
Time Complexity: O(n^2)
Space Complexity: O(1)
'''