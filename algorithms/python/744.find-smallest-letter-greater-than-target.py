#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
#
# algorithms
# Easy (45.65%)
# Likes:    2781
# Dislikes: 1985
# Total Accepted:    288.2K
# Total Submissions: 628.9K
# Testcase Example:  '["c","f","j"]\n"a"'
#
# You are given an array of characters letters that is sorted in non-decreasing
# order, and a character target. There are at least two different characters in
# letters.
# 
# Return the smallest character in letters that is lexicographically greater
# than target. If such a character does not exist, return the first character
# in letters.
# 
# 
# Example 1:
# 
# 
# Input: letters = ["c","f","j"], target = "a"
# Output: "c"
# Explanation: The smallest character that is lexicographically greater than
# 'a' in letters is 'c'.
# 
# 
# Example 2:
# 
# 
# Input: letters = ["c","f","j"], target = "c"
# Output: "f"
# Explanation: The smallest character that is lexicographically greater than
# 'c' in letters is 'f'.
# 
# 
# Example 3:
# 
# 
# Input: letters = ["x","x","y","y"], target = "z"
# Output: "x"
# Explanation: There are no characters in letters that is lexicographically
# greater than 'z' so we return letters[0].
# 
# 
# 
# Constraints:
# 
# 
# 2 <= letters.length <= 10^4
# letters[i] is a lowercase English letter.
# letters is sorted in non-decreasing order.
# letters contains at least two different characters.
# target is a lowercase English letter.
# 
# 
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] <= target:
            return letters[0]
        n = len(letters)
        left = -1
        right = n
        while left + 1 != right:
            mid = (left + right) >> 1
            if letters[mid] <= target:
                left = mid
            else:
                right = mid
        return letters[right] 
# @lc code=end

