#
# @lc app=leetcode id=1427 lang=python3
#
# [1427] Perform String Shifts
#

# @lc code=start
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total_shift = sum([amount * (1 if direction == 1 else -1) for direction, amount in shift])
        n = len(s)
        if total_shift == 0 or n == 0:
            return s
        total_shift = total_shift % n
        s = s[-total_shift:] + s[:-total_shift]
        return s
# @lc code=end

