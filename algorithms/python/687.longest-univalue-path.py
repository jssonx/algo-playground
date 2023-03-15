#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
#
# https://leetcode.com/problems/longest-univalue-path/description/
#
# algorithms
# Medium (40.34%)
# Likes:    3782
# Dislikes: 642
# Total Accepted:    161.2K
# Total Submissions: 398.9K
# Testcase Example:  '[5,4,5,1,1,null,5]'
#
# Given the root of a binary tree, return the length of the longest path, where
# each node in the path has the same value. This path may or may not pass
# through the root.
# 
# The length of the path between two nodes is represented by the number of
# edges between them.
# 
# 
# Example 1:
# 
# 
# Input: root = [5,4,5,1,1,null,5]
# Output: 2
# Explanation: The shown image shows that the longest path of the same value
# (i.e. 5).
# 
# 
# Example 2:
# 
# 
# Input: root = [1,4,5,4,4,null,5]
# Output: 2
# Explanation: The shown image shows that the longest path of the same value
# (i.e. 4).
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 10^4].
# -1000 <= Node.val <= 1000
# The depth of the tree will not exceed 1000.
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
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        if not root:
            return 0
        self.helper(root)
        return self.res
    
    def helper(self, root):
        if not root:
            return 0
        
        left_len = self.helper(root.left)
        right_len = self.helper(root.right)
        
        left_path = left_len + 1 if root.left and root.left.val == root.val else 0
        right_path = right_len + 1 if root.right and root.right.val == root.val else 0
        
        self.res = max(self.res, left_path + right_path)
        
        return max(left_path, right_path)
# @lc code=end

