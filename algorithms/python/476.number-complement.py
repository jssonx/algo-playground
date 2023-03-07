#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        binary_str = bin(num)[2:]
        comp_str = ''
        for d in binary_str:
            comp_digit = '1' if d == '0' else '0'
            comp_str += comp_digit
        res = int(comp_str, 2)
        return res
# @lc code=end

