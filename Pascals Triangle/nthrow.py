'''
Given the nth row, print all the possible values of pascal's triangle

Time Complexity: O(n)
where n is no.of rows

'''

def nthrow(r):
    res = 1
    l = [1]
    for i in range(1, r):          #for every row r, there are r elements
        res *= r - i
        res //= i
        l.append(res)
    return l

r = 6
print(nthrow(r))