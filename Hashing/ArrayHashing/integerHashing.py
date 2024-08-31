#INTEGER COUNT USING HASHING (USING LIST)

def intergerCount(arr, n):
    l = max(arr) * [0]
    for i in range(n):
        l[arr[i] - 1] += 1
    return l


arr = [1, 3, 5, 7, 1, 3]
print(intergerCount(arr, len(arr)))