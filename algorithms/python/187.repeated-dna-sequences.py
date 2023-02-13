#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        str_map = {}
        res = set()
        l, r = 0, 9
        n = len(s)
        while (r < n):
            str_ = s[l:r+1]
            if str_ in str_map and str_map[str_] == 1:
                res.add(str_)
            else:
                str_map[str_] = 1
            l += 1
            r += 1
        return list(res)
# @lc code=end

