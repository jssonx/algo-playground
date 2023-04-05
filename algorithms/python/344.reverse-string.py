#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#
# https://leetcode.com/problems/reverse-string/description/
#
# algorithms
# Easy (76.51%)
# Likes:    6819
# Dislikes: 1042
# Total Accepted:    2M
# Total Submissions: 2.6M
# Testcase Example:  '["h","e","l","l","o"]'
#
# Write a function that reverses a string. The input string is given as an
# array of characters s.
# 
# You must do this by modifying the input array in-place with O(1) extra
# memory.
# 
# 
# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s[i] is a printable ascii character.
# 
# 
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = 0
        n = len(s)
        r = n - 1
        while l <= r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
# @lc code=end

