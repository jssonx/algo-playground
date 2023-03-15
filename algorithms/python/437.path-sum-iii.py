#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#
# https://leetcode.com/problems/path-sum-iii/description/
#
# algorithms
# Medium (48.27%)
# Likes:    9330
# Dislikes: 451
# Total Accepted:    443.7K
# Total Submissions: 923.1K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# Given the root of a binary tree and an integer targetSum, return the number
# of paths where the sum of the values along the path equals targetSum.
# 
# The path does not need to start or end at the root or a leaf, but it must go
# downwards (i.e., traveling only from parent nodes to child nodes).
# 
# 
# Example 1:
# 
# 
# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.
# 
# 
# Example 2:
# 
# 
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [0, 1000].
# -10^9 <= Node.val <= 10^9
# -1000 <= targetSum <= 1000
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        if not root:
            return 0
        self.pathSumHelper(root, targetSum, [])
        return self.count
    
    def pathSumHelper(self, root, targetSum, path):
        if not root:
            return
        
        for i in range(len(path)):
            path[i] += root.val
            if path[i] == targetSum:
                self.count += 1
        path.append(root.val)
        if root.val == targetSum:
            self.count += 1
        
        self.pathSumHelper(root.left, targetSum, path)
        self.pathSumHelper(root.right, targetSum, path)
        
        path.pop()
        for i in range(len(path)):
            path[i] -= root.val
# @lc code=end

