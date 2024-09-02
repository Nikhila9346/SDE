def buyandSell(arr):
    n = len(arr)
    max_profit = 0
    min_cost = arr[0]

    for i in range(1, n):
        cost = arr[i] - min_cost
        if max_profit < cost:
            max_profit = cost
        if min_cost > arr[i]:
            min_cost = arr[i]
    return max_profit


arr = [7, 1, 5, 3, 6, 4]
# arr = [7,6,4,3,1]
print(buyandSell(arr))