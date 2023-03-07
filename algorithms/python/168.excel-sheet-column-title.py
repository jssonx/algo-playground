#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        while columnNumber > 0:
            rem = (columnNumber - 1) % 26
            res = chr(ord('A') + rem) + res
            columnNumber = (columnNumber - 1) // 26
        return res
# @lc code=end

