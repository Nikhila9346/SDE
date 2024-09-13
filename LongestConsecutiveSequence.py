'''
OBSERVATION:
If the previous element is not present that means it is the starting point of the sequence

1. Iterate through the set
2. For every element (i), check whether (i-1)th element is in the array
    (i) If yes --> go to the next element
    (ii) If no --> increase count by 1 (that means it is the starting point of the sequence) and also check if (i+1)th, (i+2)th... elements are also present by increasing count values
3. Update the maxi_len everytime by comparing it with the count
4. And whenever you don't find any (i+n)th element, make count = 1

Time Complexity: O(n)
Space Complexity: O(n)
'''

def LongestConsecutive(arr):
    count = 1
    maxi_len = 0
    nums = set(arr)
    for i in nums:
        if i-1 not in nums:
            start = i
            while (start+1) in nums:
                count += 1
                start = start + 1
            if count > maxi_len:
                maxi_len = count
        count = 1
    return maxi_len

arr = [5, 8, 3, 2, 1, 1, 4]
arr = [102, 4, 100, 1, 101, 3, 2, 1, 1]
print(LongestConsecutive(arr))