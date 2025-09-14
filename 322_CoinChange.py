class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}

        def dfs(remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')
            if remaining in memo:
                return memo[remaining]

            min_coins = float('inf')
            for coin in coins:
                min_coins = min(min_coins, 1 + dfs(remaining - coin))

            memo[remaining] = min_coins
            return min_coins

        result = dfs(amount)
        return -1 if result == float('inf') else result