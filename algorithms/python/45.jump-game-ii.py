#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        # j位置能前进的最大举例为distance[j]
        distance = nums
        n = len(distance)
        # 到dp[n]的最小步数
        dp = [0] * (n)
        j = 0
        for i in range(1, n):
            while (j + distance[j] < i):
                j += 1
            dp[i] = dp[j] + 1
        return dp[n-1]
        
# @lc code=end

