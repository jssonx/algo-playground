#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        def dp(i):
            if i >= n - 1: return True
            if i + nums[i] >= n - 1: return True
            for step in range(1, nums[i] + 1):
                if dp(i + step):
                    return True
            return False
        
        return dp(0)
        
# @lc code=end

'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_distance = 0
        n = len(nums)
        for i in range(0, n):
            if (max_distance < i):
                return False
            max_distance = max(max_distance, i + nums[i])
        return True
'''