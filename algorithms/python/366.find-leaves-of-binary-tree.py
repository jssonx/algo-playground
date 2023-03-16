#
# @lc app=leetcode id=366 lang=python3
#
# [366] Find Leaves of Binary Tree
#
# https://leetcode.com/problems/find-leaves-of-binary-tree/description/
#
# algorithms
# Medium (80.29%)
# Likes:    3041
# Dislikes: 53
# Total Accepted:    234.6K
# Total Submissions: 292.2K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given the root of a binary tree, collect a tree's nodes as if you were doing
# this:
# 
# 
# Collect all the leaf nodes.
# Remove all the leaf nodes.
# Repeat until the tree is empty.
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,4,5]
# Output: [[4,5,3],[2],[1]]
# Explanation:
# [[3,5,4],[2],[1]] and [[3,4,5],[2],[1]] are also considered correct answers
# since per each level it does not matter the order on which elements are
# returned.
# 
# 
# Example 2:
# 
# 
# Input: root = [1]
# Output: [[1]]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 100].
# -100 <= Node.val <= 100
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
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        leaves = []
        self.findLeavesHelper(root, leaves)
        return leaves

    def findLeavesHelper(self, root: Optional[TreeNode], leaves: List[List[int]]) -> int:
        if root is None:
            return -1
        left_depth = self.findLeavesHelper(root.left, leaves)
        right_depth = self.findLeavesHelper(root.right, leaves)
        current_depth = max(left_depth, right_depth) + 1
        if current_depth >= len(leaves):
            leaves.append([])
        leaves[current_depth].append(root.val)
        root.left = None
        root.right = None
        return current_depth
        
# @lc code=end

