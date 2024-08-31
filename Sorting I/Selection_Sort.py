def SelectionSort(arr, n):
    for i in range(n-1):
        min_i = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr


arr = [1, 3, 4, 7, 9]
print(SelectionSort(arr, len(arr)))

#[1, 3, 4, 7, 9]

'''
Time Complexity: Theta(n^2)
Space Complexity: Theta(1)
'''