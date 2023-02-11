#
# @lc app=leetcode id=740 lang=python3
#
# [740] Delete and Earn
#

# @lc code=start
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_num = max(nums)
        nums_new = [0] * (max_num+1)
        for num in nums:
            nums_new[num] += 1
        n = max_num + 1
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = nums_new[0]
        for k in range(2, n+1):
            op_1 = dp[k-1]
            op_2 = dp[k-2]+(k-1)*nums_new[k-1]
            dp[k] = max(op_1, op_2)
        return dp[n]

        
# @lc code=end

