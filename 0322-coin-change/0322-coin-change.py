class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        n = len(coins)
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                cur = i + coin
                if cur <= amount:
                    dp[cur] = min(dp[cur], dp[i] + 1)
        ret = dp[amount]
        if ret == float('inf'):
            return -1
        return ret
