#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#
# https://leetcode.com/problems/range-sum-of-bst/description/
#
# algorithms
# Easy (85.88%)
# Likes:    5716
# Dislikes: 352
# Total Accepted:    777.2K
# Total Submissions: 905.2K
# Testcase Example:  '[10,5,15,3,7,null,18]\n7\n15'
#
# Given the root node of a binary search tree and two integers low and high,
# return the sum of values of all nodes with a value in the inclusive range
# [low, high].
# 
# 
# Example 1:
# 
# 
# Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
# Output: 32
# Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 =
# 32.
# 
# 
# Example 2:
# 
# 
# Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
# Output: 23
# Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 =
# 23.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 2 * 10^4].
# 1 <= Node.val <= 10^5
# 1 <= low <= high <= 10^5
# All Node.val are unique.
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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0
            if low <= node.val <= high:
                return node.val + dfs(node.left) + dfs(node.right)
            
            if node.val < low:
                return dfs(node.right)
            
            if node.val > high:
                return dfs(node.left)
        
        return dfs(root)
# @lc code=end

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
class Solution:
def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
    self.total_sum = 0
    self.inorder(root, low, high)
    return self.total_sum

def inorder(self, node, low, high):
    if node is None:
        return
    self.inorder(node.left, low, high)
    if low <= node.val <= high:
        self.total_sum += node.val
    self.inorder(node.right, low, high)
'''