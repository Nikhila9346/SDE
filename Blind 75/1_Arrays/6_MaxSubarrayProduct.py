#152

def maxProduct(nums):
    max_prod = nums[0]
    prefix = 1
    postfix = 1

    for i in range(len(nums)):
        prefix = 1 if prefix == 0 else prefix
        postfix = 1 if postfix == 0 else postfix

        prefix *= nums[i]
        # print(prefix)
        postfix *= nums[len(nums)-i-1]
        # print(postfix)
        max_prod = max(max_prod, max(prefix, postfix))
    
    return max_prod


nums = [2,3,-2,4]
nums = [-4, -3]
print(maxProduct(nums))   #6