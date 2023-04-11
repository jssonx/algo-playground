#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (38.94%)
# Likes:    20482
# Dislikes: 1233
# Total Accepted:    2M
# Total Submissions: 5M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# There is an integer array nums sorted in ascending order (with distinct
# values).
# 
# Prior to being passed to your function, nums is possibly rotated at an
# unknown pivot index k (1 <= k < nums.length) such that the resulting array is
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
# (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3
# and become [4,5,6,7,0,1,2].
# 
# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start

# 0 1 2 4 5 6 7
# 4 5 6 7 0 1 2
# target: 0
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1
        l, r = -1, n
        while l + 1 != r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # 有限区间内是有序的，因此可以做判断
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid
                else:
                    l = mid
            else:
                if nums[mid] < target <= nums[n - 1]:
                    l = mid
                else:
                    r = mid
        return -1
# @lc code=end

