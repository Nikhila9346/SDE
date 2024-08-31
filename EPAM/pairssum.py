#find the no.of pairs which will add up to the given sum

def pairsSum(arr, target):
    hashMap = {}   #val: index
    cout = 0
    for ind, val in enumerate(arr):
        diff = target - val
        if diff not in hashMap:
            hashMap[val] = ind
        else:
            cout += 1

    return cout


arr = [3, 4, 2, 1, 2, 3, 5]
print(pairsSum(arr, 6))