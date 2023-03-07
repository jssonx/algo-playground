#
# @lc app=leetcode id=717 lang=python3
#
# [717] 1-bit and 2-bit Characters
#

# @lc code=start
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        while i < len(bits) - 1:
            if bits[i] == 0:
                i += 1
            else:
                i += 2
        return i == len(bits) - 1
# @lc code=end

