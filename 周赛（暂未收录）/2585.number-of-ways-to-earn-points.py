class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        dp = [[0] * (target + 1) for _ in range(len(types) + 1)]
        for i in range(len(types) + 1):
            dp[i][0] = 1
        for i in range(1, len(types) + 1):
            for j in range(1, target + 1):
                count = 0
                for k in range(types[i-1][0] + 1):
                    if j - k * types[i-1][1] < 0:
                        break
                    count += dp[i-1][j-k*types[i-1][1]]
                dp[i][j] = count % 1000000007
        return dp[len(types)][target]