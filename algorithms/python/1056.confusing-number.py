#
# @lc app=leetcode id=1056 lang=python3
#
# [1056] Confusing Number
#

# @lc code=start
class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotate = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        s = str(n)
        rotated = ''
        for i in range(len(s)):
            if s[i] not in rotate:
                return False
            rotated += rotate[s[i]]
        return rotated[::-1] != s
# @lc code=end

