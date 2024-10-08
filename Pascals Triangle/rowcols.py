'''
Given r and c value, find the value in pascals triangle

To calculate the value at some row and column, we use formula (N-1)c(r-1) = n!/r! * (n-r)! which is a brute force approach
Can reduce the time complexity, by formula = n*(n-1)..(r times)/r!

where n --> no.of rows
      c --> no.of cols

Time Complexity: O(c)
'''

def pascals(r, c):
    res = 1
    for i in range(c):
        res *= (r-i)
        res //= (i+1)

    return res

r = 5
c = 3
print(pascals(r-1, c-1))