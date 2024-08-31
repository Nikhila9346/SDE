#HIGHEST AND LOWEST FREQUENCY OF AN ELEMENT

'''
Input: array[] = {10,5,10,15,10,5};
Output: 10 15
Explanation: The frequency of 10 is 3, i.e. the highest and the frequency of 15 is 1 i.e. the lowest.

'''
def highlowFrequency(arr, n):
    d = {}
    for i in arr:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    max = float('-inf')
    min = float('inf')
    for val, freq in d.items():
        if freq > max:
            max = val
        if freq < min:
            min = val
    return max, min

arr = [10, 5, 10, 15, 10, 5]
print(highlowFrequency(arr, len(arr)))      #(10, 15)