#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (41.83%)
# Likes:    16472
# Dislikes: 393
# Total Accepted:    1.5M
# Total Submissions: 3.6M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in non-decreasing order, find the
# starting and ending position of a given target value.
# 
# If target is not found in the array, return [-1, -1].
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums is a non-decreasing array.
# -10^9 <= target <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = -1, len(nums)
        start, end = -1, -1
        while left + 1 != right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                start, end = mid, mid
                while start > 0 and nums[start-1] == target:
                    start -= 1
                while end < len(nums)-1 and nums[end+1] == target:
                    end += 1
                return [start, end]
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        return [start, end]
        
# @lc code=end

