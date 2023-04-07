#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#
# https://leetcode.com/problems/decode-string/description/
#
# algorithms
# Medium (57.86%)
# Likes:    10602
# Dislikes: 480
# Total Accepted:    631.4K
# Total Submissions: 1.1M
# Testcase Example:  '"3[a]2[bc]"'
#
# Given an encoded string, return its decoded string.
# 
# The encoding rule is: k[encoded_string], where the encoded_string inside the
# square brackets is being repeated exactly k times. Note that k is guaranteed
# to be a positive integer.
# 
# You may assume that the input string is always valid; there are no extra
# white spaces, square brackets are well-formed, etc. Furthermore, you may
# assume that the original data does not contain any digits and that digits are
# only for those repeat numbers, k. For example, there will not be input like
# 3a or 2[4].
# 
# The test cases are generated so that the length of the output will never
# exceed 10^5.
# 
# 
# Example 1:
# 
# 
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# 
# 
# Example 2:
# 
# 
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# 
# 
# Example 3:
# 
# 
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets
# '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].
# 
# 
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        k = 0
        for ch in s:
            if ch.isdigit():
                k = k * 10 + int(ch)   # 处理连续的数字
            elif ch == '[':
                stack.append((res, k))
                res = ""
                k = 0
            elif ch == ']':
                prev_str, prev_k = stack.pop()
                res = prev_str + prev_k * res
            else:
                res += ch
        return res
        
# @lc code=end

