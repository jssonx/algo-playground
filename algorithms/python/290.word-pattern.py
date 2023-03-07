#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        p_to_s = {}
        s_to_p = {}
        
        for i in range(len(pattern)):
            if pattern[i] not in p_to_s and words[i] not in s_to_p:
                p_to_s[pattern[i]] = words[i]
                s_to_p[words[i]] = pattern[i]
            elif pattern[i] in p_to_s and words[i] != p_to_s[pattern[i]]:
                return False
            elif words[i] in s_to_p and pattern[i] !=  s_to_p[words[i]]:
                return False
        
        return True
        
# @lc code=end

