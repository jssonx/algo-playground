#
# @lc app=leetcode id=666 lang=python3
#
# [666] Path Sum IV
#
# https://leetcode.com/problems/path-sum-iv/description/
#
# algorithms
# Medium (59.39%)
# Likes:    319
# Dislikes: 411
# Total Accepted:    21.4K
# Total Submissions: 36K
# Testcase Example:  '[113,215,221]'
#
# If the depth of a tree is smaller than 5, then this tree can be represented
# by an array of three-digit integers. For each integer in this array:
# 
# 
# The hundreds digit represents the depth d of this node where 1 <= d <= 4.
# The tens digit represents the position p of this node in the level it belongs
# to where 1 <= p <= 8. The position is the same as that in a full binary
# tree.
# The units digit represents the value v of this node where 0 <= v <= 9.
# 
# 
# Given an array of ascending three-digit integers nums representing a binary
# tree with a depth smaller than 5, return the sum of all paths from the root
# towards the leaves.
# 
# It is guaranteed that the given array represents a valid connected binary
# tree.
# 
# 
# Example 1:
# 
# 
# Input: nums = [113,215,221]
# Output: 12
# Explanation: The tree that the list represents is shown.
# The path sum is (3 + 5) + (3 + 1) = 12.
# 
# 
# Example 2:
# 
# 
# Input: nums = [113,221]
# Output: 4
# Explanation: The tree that the list represents is shown. 
# The path sum is (3 + 1) = 4.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 15
# 110 <= nums[i] <= 489
# nums represents a valid binary tree with depth less than 5.
# 
# 
#

# @lc code=start
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        tree = {}
        for num in nums:
            d, p, v = num // 100, num % 100 // 10, num % 10
            tree[(d, p)] = v
        self.res = 0
        self.dfs(tree, 1, 1, 0)
        return self.res
    
    def dfs(self, tree, d, p, cur_sum):
        if (d, p) not in tree:
            return
        cur_sum += tree[(d, p)]
        # no child node here
        if (d + 1, p * 2 - 1) not in tree and (d + 1, p * 2) not in tree:
            self.res += cur_sum
        else:
            self.dfs(tree, d + 1, p * 2 - 1, cur_sum)
            self.dfs(tree, d + 1, p * 2, cur_sum)
        
# @lc code=end

