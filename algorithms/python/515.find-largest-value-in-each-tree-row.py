#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
#
# algorithms
# Medium (64.54%)
# Likes:    2685
# Dislikes: 95
# Total Accepted:    229.5K
# Total Submissions: 355.5K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# Given the root of a binary tree, return an array of the largest value in each
# row of the tree (0-indexed).
# 
# 
# Example 1:
# 
# 
# Input: root = [1,3,2,5,3,null,9]
# Output: [1,3,9]
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,3]
# Output: [1,3]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree will be in the range [0, 10^4].
# -2^31 <= Node.val <= 2^31 - 1
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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        queue = [root]
        while len(queue) > 0:
            max = queue[0].val
            length = len(queue)
            for i in range(length):
                node = queue.pop(0)
                if node.val > max:
                    max = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(max)
        return res
        
# @lc code=end

