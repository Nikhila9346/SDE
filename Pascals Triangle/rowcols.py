'''
Given r and c value, find the value in pascals triangle
'''

def pascals(r, c):
    res = 1
    for i in range(c):
        res *= (r-i)
        res //= (i+1)

    return res


print(pascals(10, 3))