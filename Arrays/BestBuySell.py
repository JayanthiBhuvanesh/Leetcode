def best_buy_sell(prices):
    i =0
    exp = prices[0]
    profit = 0
    while i < len(prices):
        exp = min(exp, prices[i])
        profit = max(profit, prices[i]-exp)
        i+=1
    return profit

print(best_buy_sell([7, 1, 5, 3, 6, 8]))