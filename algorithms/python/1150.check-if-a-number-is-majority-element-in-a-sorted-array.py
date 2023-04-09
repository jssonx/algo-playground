#
# @lc app=leetcode id=1150 lang=python3
#
# [1150] Check If a Number Is Majority Element in a Sorted Array
#
# https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/description/
#
# algorithms
# Easy (57.18%)
# Likes:    373
# Dislikes: 34
# Total Accepted:    38.3K
# Total Submissions: 67K
# Testcase Example:  '[2,4,5,5,5,5,5,6,6]\n5'
#
# Given an integer array nums sorted in non-decreasing order and an integer
# target, return true if target is a majority element, or false otherwise.
# 
# A majority element in an array nums is an element that appears more than
# nums.length / 2 times in the array.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
# Output: true
# Explanation: The value 5 appears 5 times and the length of the array is 9.
# Thus, 5 is a majority element because 5 > 9/2 is true.
# 
# 
# Example 2:
# 
# 
# Input: nums = [10,100,101,101], target = 101
# Output: false
# Explanation: The value 101 appears 2 times and the length of the array is 4.
# Thus, 101 is not a majority element because 2 > 4/2 is false.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 1000
# 1 <= nums[i], target <= 10^9
# nums is sorted in non-decreasing order.
# 
# 
#

# @lc code=start
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # 找到第一个等于 target 的数，和第一个大于 target 的数
        n = len(nums)
        left = -1
        right = n
        while left + 1 != right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid
            else:
                right = mid
        left_bound = right

        left = -1
        right = n
        while left + 1 != right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        right_bound = right
        if right_bound - left_bound > n / 2:
            return True
        else:
            return False
# @lc code=end

