#find the number of elements which is occuring odd number of times

def oddTimes(arr):
    hashMap = {}
    for i in arr:
        if i in hashMap:
            hashMap[i] += 1
        else:
            hashMap[i] = 1
    count = 0
    for i in hashMap.values():
        if i%2 != 0:
            count += 1
    return count

arr = [1, 2, 4, 6, 6, 1, 1]
print(oddTimes(arr))