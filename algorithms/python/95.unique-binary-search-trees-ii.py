#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (52.28%)
# Likes:    5771
# Dislikes: 376
# Total Accepted:    348.1K
# Total Submissions: 665.7K
# Testcase Example:  '3'
#
# Given an integer n, return all the structurally unique BST's (binary search
# trees), which has exactly n nodes of unique values from 1 to n. Return the
# answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: n = 3
# Output:
# [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
# 
# 
# Example 2:
# 
# 
# Input: n = 1
# Output: [[1]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 8
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
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def node(val, left, right):
            node = TreeNode(val)
            node.left = left
            node.right = right
            return node
        def trees(first, last):
            return [node(root, left, right)
                    for root in range(first, last+1)
                    for left in trees(first, root-1)
                    for right in trees(root+1, last)] or [None]
        return trees(1, n)
        
# @lc code=end

