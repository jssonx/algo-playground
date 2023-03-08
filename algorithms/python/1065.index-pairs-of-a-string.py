#
# @lc app=leetcode id=1065 lang=python3
#
# [1065] Index Pairs of a String
#

# @lc code=start
import re
from typing import List
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        res = []
        
        for w in words:
            for m in re.finditer('(?={0})'.format(w), text):
                start_index = m.start()
                end_index = start_index + len(w) - 1                
                index_pair = [start_index, end_index]
                res.append(index_pair)
        
        res.sort()        
        return res
# @lc code=end

