class Solution:
    def maxProfit(self, prices) -> int:
        i = 0
        profit = 0
        while i < len(prices):
            if i + 1 < len(prices) and prices[i] <= prices[i + 1]:
                buy = prices[i]
                while prices[i] <= prices[i + 1]:
                    i += 1
                sell = prices[i]

                profit += sell - buy
                i += 1
            else:
                i += 1
        return profit

if __name__ == '__main__':

    print(Solution().maxProfit([7, 5, 4]))
