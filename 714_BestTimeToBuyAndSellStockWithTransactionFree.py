class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        n = len(prices)
        memo = {}
        def dfs(day, holding):
            if day >= n:
                return 0
            if (day, holding) in memo:
                return memo[(day, holding)]
            
            best = dfs(day + 1, holding)
            if holding:
                best = max(best, prices[day] - fee + dfs(day + 1, 0))
            else:
                best = max(best, -prices[day] + dfs(day + 1, 1))
            memo[(day, holding)] = best
            return best
        return dfs(0, 0)