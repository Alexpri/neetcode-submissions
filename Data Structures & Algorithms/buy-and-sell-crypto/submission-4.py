class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        len_prices = len(prices)
        min_pointer = 0
        min_value = prices[0]
        max_pointer = 1
        max_value = 0
        profit = 0

        while max_pointer < len_prices:
            if prices[max_pointer] > prices[min_pointer]:
                differece = prices[max_pointer] - prices[min_pointer]
                profit = max(differece, profit)
            else:
                min_pointer = max_pointer

            max_pointer += 1

        return profit

