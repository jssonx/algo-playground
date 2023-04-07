#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (36.05%)
# Likes:    7498
# Dislikes: 1350
# Total Accepted:    705.6K
# Total Submissions: 2M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given the head of a linked list, rotate the list to the right by k places.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# 
# 
# Example 2:
# 
# 
# Input: head = [0,1,2], k = 4
# Output: [2,0,1]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [0, 500].
# -100 <= Node.val <= 100
# 0 <= k <= 2 * 10^9
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:    
        if not head:
            return head
        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1
        k %= n
        slow = fast = head
        for i in range(k):
            fast = fast.next
        while fast.next:
            slow, fast = slow.next, fast.next
        fast.next = head
        head = slow.next
        slow.next = None
        return head
        
# @lc code=end

