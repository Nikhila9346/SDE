#COUNT THE FREQUENCY OF ELEMENTS USING DICTIONARY HASHING

def count(arr, n):
    d = {}
    for i in arr:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d


arr = [1, 3, 5, 2, 5, 3]       #{1: 1, 3: 2, 5: 2, 2: 1}
arr = 'ababacghde'             #{'a': 3, 'b': 2, 'c': 1, 'g': 1, 'h': 1, 'd': 1, 'e': 1}
print(count(arr, len(arr)))