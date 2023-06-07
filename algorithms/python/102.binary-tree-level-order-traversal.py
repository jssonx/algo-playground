#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (64.69%)
# Likes:    13244
# Dislikes: 265
# Total Accepted:    1.8M
# Total Submissions: 2.8M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given the root of a binary tree, return the level order traversal of its
# nodes' values. (i.e., from left to right, level by level).
# 
# 
# Example 1:
# 
# 
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
# 
# 
# Example 2:
# 
# 
# Input: root = [1]
# Output: [[1]]
# 
# 
# Example 3:
# 
# 
# Input: root = []
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 2000].
# -1000 <= Node.val <= 1000
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = []
        queue.append(root)
        topo = []
        while len(queue) > 0:
            subtopo = []
            for _ in range(len(queue)):
                cur = queue.pop(0)
                subtopo.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            topo.append(subtopo)
        return topo
        
        
# @lc code=end

