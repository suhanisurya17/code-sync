class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #max_profit = 0
        # for sell in range(len(prices)):
        #     for buy in range(len(prices)):
        #         if sell != buy and sell > buy:
        #             profit = prices[sell] - prices[buy]
        #             if profit > max_profit:
        #                 max_profit = profit
        # return max_profit

        #this solution has time complexity of o(n^2)

        #using hash maps like 2 sum
        max_profit = 0
        min_price = float('inf') #this number is infinity

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit
