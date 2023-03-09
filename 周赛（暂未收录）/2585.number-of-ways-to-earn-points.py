# dp[i][j]: the number of ways you can earn exactly j points in the exam from tne first i types
class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        n = len(types)
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(1, n+1):
            for j in range(1, target+1):
                for k in range(types[i-1][0]+1):
                    if k*types[i-1][1] > j:
                        break
                    dp[i][j] += dp[i-1][j-k*types[i-1][1]]
                    dp[i][j] %= 1000000007
        return dp[n][target]