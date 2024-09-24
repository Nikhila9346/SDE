def RotateMatrix(nums):
    n = len(nums) #no.of rows and
    for i in range(n):
        for j in range(n):
            if i!=j:
                nums[i][j], nums[j][i] = nums[j][i], nums[i][j]
    # for i in range(n):
    #     for j in range(n//2):
    #         nums[i][j], nums[i][n-1-i] = nums[i][n-1-i], nums[i][j]

    return nums

nums = [[1,2,3],[4,5,6],[7,8,9]]
print(RotateMatrix(nums))

'''
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

[[1, 4, 7],
 [4, 5, 8],
 [7, 8, 9]]
'''