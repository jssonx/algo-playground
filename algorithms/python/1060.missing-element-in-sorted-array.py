#
# @lc app=leetcode id=1060 lang=python3
#
# [1060] Missing Element in Sorted Array
#
# https://leetcode.com/problems/missing-element-in-sorted-array/description/
#
# algorithms
# Medium (54.71%)
# Likes:    1478
# Dislikes: 57
# Total Accepted:    112.9K
# Total Submissions: 206.1K
# Testcase Example:  '[4,7,9,10]\n1'
#
# Given an integer array nums which is sorted in ascending order and all of its
# elements are unique and given also an integer k, return the k^th missing
# number starting from the leftmost number of the array.
# 
# 
# Example 1:
# 
# 
# Input: nums = [4,7,9,10], k = 1
# Output: 5
# Explanation: The first missing number is 5.
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,7,9,10], k = 3
# Output: 8
# Explanation: The missing numbers are [5,6,8,...], hence the third missing
# number is 8.
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,4], k = 3
# Output: 6
# Explanation: The missing numbers are [3,5,6,7,...], hence the third missing
# number is 6.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5 * 10^4
# 1 <= nums[i] <= 10^7
# nums is sorted in ascending order, and all the elements are unique.
# 1 <= k <= 10^8
# 
# 
# 
# Follow up: Can you find a logarithmic time complexity (i.e., O(log(n)))
# solution?
#

# @lc code=start
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        left = -1
        right = len(nums)
        while left + 1 != right:
            mid = (left + right) // 2
            missing_num_left = nums[mid] - mid - nums[0]
            if missing_num_left >= k:
                right = mid
            else:
                left = mid
        res = k + left + nums[0]
        return res
# @lc code=end

