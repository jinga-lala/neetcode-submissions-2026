class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 1e9
        right = 0
        ans = 0
        for i in range(len(prices)):
            if prices[i] < left:
                ans = max(ans, right-left)
                left= prices[i]
                right = prices[i]
            elif prices[i] > right:
                right = prices[i]
            # print(ans, left, right)
        ans = max(ans, right-left)
        
        return ans