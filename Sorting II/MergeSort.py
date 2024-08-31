def mergeSort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, high)
    merge(arr, low, mid, high)

def merge(arr, low, mid, high):
    left = low
    right = mid + 1
    temp = []
    while(left <= mid and right <= high):
        if arr[left] > arr[right]:
            temp.append(arr[right])
            right += 1
        else:
            temp.append(arr[left])
            left += 1
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high+1):
        arr[i] = temp[i - low]
    

arr = [9, 14, 16, 19, 6, 12]
mergeSort(arr, 0, len(arr)-1)
print(arr)                         

#[6, 9, 12, 14, 16, 19]