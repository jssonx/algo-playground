#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#
# https://leetcode.com/problems/reverse-only-letters/description/
#
# algorithms
# Easy (61.95%)
# Likes:    1841
# Dislikes: 62
# Total Accepted:    162.1K
# Total Submissions: 261K
# Testcase Example:  '"ab-cd"'
#
# Given a string s, reverse the string according to the following rules:
# 
# 
# All the characters that are not English letters remain in the same
# position.
# All the English letters (lowercase or uppercase) should be reversed.
# 
# 
# Return s after reversing it.
# 
# 
# Example 1:
# Input: s = "ab-cd"
# Output: "dc-ba"
# Example 2:
# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:
# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 100
# s consists of characters with ASCII values in the range [33, 122].
# s does not contain '\"' or '\\'.
# 
# 
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            if not self.isLetter(s[left]):
                left += 1
            if not self.isLetter(s[right]):
                right -= 1
            if self.isLetter(s[left]) and self.isLetter(s[right]):
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        return "".join(s)
    
    def isLetter(self, char):
        return ord('a') <= ord(char) <= ord('z') or ord('A') <= ord(char) <= ord('Z')
# @lc code=end

