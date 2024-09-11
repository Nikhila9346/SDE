import heapq
def MinimumCostofRopes(nums):
    heapq.heapify(nums)

    cost = 0
    for i in range(len(nums)-1):
        add = heapq.heappop(nums) + heapq.heappop(nums)
        cost += add

        heapq.heappush(nums, add)

    return cost


nums = [4, 3, 2, 6]
nums = [4, 2, 7, 6, 9]
print(MinimumCostofRopes(nums))