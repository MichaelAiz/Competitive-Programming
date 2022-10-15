class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]
        numWays = 0
        if n <= 2:
            return n
        for i in range (3, n+1):
            numWays = dp[1] + dp[0]
            dp[0] = dp[1]
            dp[1] = numWays
        return numWays