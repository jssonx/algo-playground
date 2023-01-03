#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i in range(len(nums)):
            tmp = nums[i]
            s[tmp] = i
        for i in range(len(nums)):
            tmp = nums[i]
            comp = target - tmp
            if comp in s and s[comp] != i:
                return [i, s[comp]]

        
# @lc code=end

