def max_profit(prices):
    if len(prices) < 2:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    
    for x in prices[1:]:
        profit = x - min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, x)
    
    return max_profit



n = int(input())
prices = []

for i in range(n):
    prices.append(int(input()))


print(max_profit(prices))
