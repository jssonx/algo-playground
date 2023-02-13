#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        n = len(s)
        i = 0
        res = 0
        for j in range(0, n):
            if s[j] in char_map:
                i = max(i, char_map[s[j]] + 1)
            char_map[s[j]] = j
            res = max(res, j - i + 1)
        return res
# @lc code=end

