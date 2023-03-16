#
# @lc app=leetcode id=889 lang=python3
#
# [889] Construct Binary Tree from Preorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/
#
# algorithms
# Medium (70.96%)
# Likes:    2410
# Dislikes: 97
# Total Accepted:    86.8K
# Total Submissions: 122.3K
# Testcase Example:  '[1,2,4,5,3,6,7]\n[4,5,2,6,7,3,1]'
#
# Given two integer arrays, preorder and postorder where preorder is the
# preorder traversal of a binary tree of distinct values and postorder is the
# postorder traversal of the same tree, reconstruct and return the binary
# tree.
# 
# If there exist multiple answers, you can return any of them.
# 
# 
# Example 1:
# 
# 
# Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]
# 
# 
# Example 2:
# 
# 
# Input: preorder = [1], postorder = [1]
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= preorder.length <= 30
# 1 <= preorder[i] <= preorder.length
# All the values of preorder are unique.
# postorder.length == preorder.length
# 1 <= postorder[i] <= postorder.length
# All the values of postorder are unique.
# It is guaranteed that preorder and postorder are the preorder traversal and
# postorder traversal of the same binary tree.
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
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None

        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root

        # Find the index of the root in postorder
        root_idx = postorder.index(preorder[1])

        # Construct left and right subtrees
        root.left = self.constructFromPrePost(preorder[1:root_idx+2], postorder[:root_idx+1])
        root.right = self.constructFromPrePost(preorder[root_idx+2:], postorder[root_idx+1:-1])

        return root

        
# @lc code=end

