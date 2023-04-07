#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#
# https://leetcode.com/problems/shortest-palindrome/description/
#
# algorithms
# Hard (32.33%)
# Likes:    3094
# Dislikes: 218
# Total Accepted:    154.5K
# Total Submissions: 477.6K
# Testcase Example:  '"aacecaaa"'
#
# You are given a string s. You can convert s to a palindrome by adding
# characters in front of it.
# 
# Return the shortest palindrome you can find by performing this
# transformation.
# 
# 
# Example 1:
# Input: s = "aacecaaa"
# Output: "aaacecaaa"
# Example 2:
# Input: s = "abcd"
# Output: "dcbabcd"
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 5 * 10^4
# s consists of lowercase English letters only.
# 
# 
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        pattern = s + " " + s[::-1]
        # KMP
        table = [0]
        pos = 0
        for i in range(1, len(pattern)):
            while pos != 0 and pattern[pos] != pattern[i]:
                pos = table[pos - 1]
            if pattern[pos] == pattern[i]:
                pos += 1
            table.append(pos)
        return s[table[-1]:][::-1] + s
        
# @lc code=end

