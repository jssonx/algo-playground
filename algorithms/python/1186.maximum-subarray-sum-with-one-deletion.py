#
# @lc app=leetcode id=1186 lang=python3
#
# [1186] Maximum Subarray Sum with One Deletion
#

# @lc code=start
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        res = -float('inf')
        if (n == 0):
            return 0
        elif (n == 1):
            return arr[0]
        # 0: 当前没有行使过删除权力的max
        # 1: 当前行使过删除权力的max
        dp = [[0]*2 for _ in range(n+1)]
        dp[1] = [arr[0], 0]
        for k in range(2, n+1):
            dp[k][0] = max(dp[k-1][0] + arr[k-1], arr[k-1])
            dp[k][1] =  max(dp[k-1][0], dp[k-1][1] + arr[k-1])
        for x in dp[2:]:
            res = max(res, x[0], x[1])
        return res
# @lc code=end

