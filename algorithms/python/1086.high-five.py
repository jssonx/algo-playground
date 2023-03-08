#
# @lc app=leetcode id=1086 lang=python3
#
# [1086] High Five
#

# @lc code=start
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        scores = {}
        for item in items:
            ID, score = item
            if ID not in scores:
                scores[ID] = []
            scores[ID].append(score)
        
        result = []
        for ID in sorted(scores):
            top_five = sorted(scores[ID], reverse=True)[:5]
            top_five_average = sum(top_five) // 5
            result.append([ID, top_five_average])
        
        return result
        
# @lc code=end

