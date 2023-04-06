#
# @lc app=leetcode id=270 lang=python3
#
# [270] Closest Binary Search Tree Value
#
# https://leetcode.com/problems/closest-binary-search-tree-value/description/
#
# algorithms
# Easy (54.74%)
# Likes:    1647
# Dislikes: 94
# Total Accepted:    283.2K
# Total Submissions: 517.6K
# Testcase Example:  '[4,2,5,1,3]\n3.714286'
#
# Given the root of a binary search tree and a target value, return the value
# in the BST that is closest to the target. If there are multiple answers,
# print the smallest.
# 
# 
# Example 1:
# 
# 
# Input: root = [4,2,5,1,3], target = 3.714286
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: root = [1], target = 4.428571
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# 0 <= Node.val <= 10^9
# -10^9 <= target <= 10^9
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        while root:
            if abs(root.val - target) <= abs(closest - target):
                closest = root.val
            root = root.left if target < root.val else root.right
        return closest

# @lc code=end

