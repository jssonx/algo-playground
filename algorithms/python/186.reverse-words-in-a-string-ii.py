#
# @lc app=leetcode id=186 lang=python3
#
# [186] Reverse Words in a String II
#

# @lc code=start
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        s.reverse()

        start = 0
        for i in range(len(s)):
            if s[i] == ' ':
                s[start:i] = reversed(s[start:i])
                start = i + 1

        s[start:] = reversed(s[start:])
# @lc code=end

