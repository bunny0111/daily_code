'''
You are given an array of prices where prices[i] is the price of a given stock on an ith day. You want to maximise your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
'''
def stock_buy_sell(prices):
        # Initialize min_price to infinity (inf) so any price in the list will be smaller. To represent positive infinity in Python, we use float('inf') , and for negative infinity, we use float('-inf') 
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            max_profit = max(max_profit, profit)
    return max_profit

prices = [7,1,5,3,6,4]
print(stock_buy_sell(prices))