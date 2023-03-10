#
# @lc app=leetcode id=2357 lang=python3
#
# [2357] Make Array Zero by Subtracting Equal Amounts
#

# @lc code=start
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = set(nums)
        if 0 in nums:
            nums.remove(0)
        return len(nums)
# @lc code=end

