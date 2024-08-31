#CHARACTER COUNT USING HASHING (USING ARRAY)

def characterCount(arr, n):
    l = 26 * [0]
    for i in range(n):
        l[ord(arr[i]) - ord('a')] += 1
    return l


arr = 'abcabde'
print(characterCount(arr, len(arr)))

