'''
Given an integer numRows, return the first numRows of Pascal's triangle.

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Explanation:

1. Run a loop for n times (where n is no.of rows)
2. For every loop, calculate the elements (no.of elements = The row number) 

Time Complexity: O(n^2)

'''
def generateRow(n):
    l = [1]
    res = 1
    for j in range(1, n):
        res *= (n-j)
        res //= j
        l.append(res)
    return l

def pascalTriangle(n):
    ans = []
    for i in range(1, n+1):
        ans.append(generateRow(i))
    return ans

n = 6
print(pascalTriangle(n))