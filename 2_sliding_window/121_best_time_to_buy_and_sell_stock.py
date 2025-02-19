class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy_price = prices[0]
        # if I can find a lower buy price, than I can adjust
        # the buy_price (this is the "sliding window" element)
        # if the difference between the buy price and current
        # price larger than max_profit than I update max profit
        for i in range(len(prices)):
            buy_price = min(prices[i], buy_price)
            current_profit = prices[i] - buy_price
            max_profit = max(current_profit, max_profit)
        return max_profit
            