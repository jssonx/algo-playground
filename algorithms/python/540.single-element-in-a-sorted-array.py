#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#
# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
#
# algorithms
# Medium (59.13%)
# Likes:    8959
# Dislikes: 137
# Total Accepted:    463.2K
# Total Submissions: 783.5K
# Testcase Example:  '[1,1,2,3,3,4,4,8,8]'
#
# You are given a sorted array consisting of only integers where every element
# appears exactly twice, except for one element which appears exactly once.
# 
# Return the single element that appears only once.
# 
# Your solution must run in O(log n) time and O(1) space.
# 
# 
# Example 1:
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 0 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = -1
        right = len(nums)
        while left + 1 != right:
            mid = (left + right) // 2
            if mid % 2 == 0:
                # mid is even
                if mid + 1 < len(nums) and nums[mid] == nums[mid+1]:
                    left = mid
                else:
                    right = mid
            else:
                # mid is odd
                if mid - 1 >= 0 and nums[mid] == nums[mid-1]:
                    left = mid
                else:
                    right = mid
        return nums[right]

# @lc code=end

# 由于给定数组有序 且 常规元素总是两两出现，因此如果不考虑“特殊”的单一元素的话，我们有结论：成对元素中的第一个所对应的下标必然是偶数，成对元素中的第二个所对应的下标必然是奇数。
# 然后再考虑存在单一元素的情况，假如单一元素所在的下标为 xxx，那么下标 xxx 之前（左边）的位置仍满足上述结论，而下标 xxx 之后（右边）的位置由于 xxx 的插入，导致结论翻转。
# return nums[right]是因为左边是闭区间