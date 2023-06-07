#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/
#
# algorithms
# Medium (66.04%)
# Likes:    1993
# Dislikes: 71
# Total Accepted:    131.7K
# Total Submissions: 199.5K
# Testcase Example:  '[1,7,0,7,-8,null,null]'
#
# Given the root of a binary tree, the level of its root is 1, the level of its
# children is 2, and so on.
# 
# Return the smallest level x such that the sum of all the values of nodes at
# level x is maximal.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.
# 
# 
# Example 2:
# 
# 
# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^4].
# -10^5 <= Node.val <= 10^5
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
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        res = 0
        level = 1
        level_sum_max = -float('inf')
        while len(queue) > 0:
            level_sum = 0
            for _ in range(len(queue)):
                cur = queue.pop(0)
                level_sum += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            if level_sum > level_sum_max:
                res = level
                level_sum_max = level_sum
            level += 1
        return res
        
# @lc code=end

