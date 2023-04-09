#
# @lc app=leetcode id=1099 lang=python3
#
# [1099] Two Sum Less Than K
#
# https://leetcode.com/problems/two-sum-less-than-k/description/
#
# algorithms
# Easy (61.02%)
# Likes:    1021
# Dislikes: 116
# Total Accepted:    115.5K
# Total Submissions: 189.2K
# Testcase Example:  '[34,23,1,24,75,33,54,8]\n60'
#
# Given an array nums of integers and integer k, return the maximum sum such
# that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j
# exist satisfying this equation, return -1.
# 
# 
# Example 1:
# 
# 
# Input: nums = [34,23,1,24,75,33,54,8], k = 60
# Output: 58
# Explanation: We can use 34 and 24 to sum 58 which is less than 60.
# 
# 
# Example 2:
# 
# 
# Input: nums = [10,20,30], k = 15
# Output: -1
# Explanation: In this case it is not possible to get a pair sum less that
# 15.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 1000
# 1 <= k <= 2000
# 
# 
#

# @lc code=start
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        res = -1
        for i in range(len(nums)):
            left = i
            right = len(nums)
            while left + 1 != right:
                mid = left + (right - left) // 2
                if nums[i] + nums[mid] < k:
                    res = max(res, nums[i] + nums[mid])
                    left = mid
                else:
                    right = mid
        return res
        
# @lc code=end

