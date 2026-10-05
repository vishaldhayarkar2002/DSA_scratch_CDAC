def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price          # new cheapest buy day
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit