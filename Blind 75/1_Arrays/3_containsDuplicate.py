#217

def containsDuplicate(arr):
    hashSet = set()
    for i in arr:
        if i in hashSet:
            return True
        hashSet.add(i)
    return False

arr = [1,2,3,1]
print(containsDuplicate(arr))   #True