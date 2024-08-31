#FREQUENCIES OF LIMITED RANGE ARRAY ELEMENTS
#? DATASTRUCTURE USED ARRAY HASHING

'''
1. add the elements of frequency list into the original list
2. ignore the elements which are greater than n

Input: n = 5, arr[] = [2, 3, 2, 3, 5], p = 5 (the list contains elements from 1 to p)
Output: [0, 2, 2, 0, 1]

Input: n = 2, arr[] = [8, 9], p = 9
Output: [0, 0]
Explanation: Counting frequencies of each array element We have: 1 occurring 0 times. 2 occurring 0 times. Since here P=9, but there are no 9th Index present so can't count the value.

'''

def feqCount(arr, n ,p):
    l = n*[0]
    for i in range(n):
        if 1 <= arr[i] <= n:
            l[arr[i] - 1] += 1
    #updating the original list
    for i in range(n):
        arr[i] = l[i]
    return l 

arr = [2, 3, 2, 3, 5]
print(feqCount(arr, len(arr), 5))