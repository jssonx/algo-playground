#
# @lc app=leetcode id=734 lang=python3
#
# [734] Sentence Similarity
#

# @lc code=start
class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        similar_set = set()
        for pair in similarPairs:
            similar_set.add(tuple(pair))
        for i in range(len(sentence1)):
            if sentence1[i] != sentence2[i] and (sentence1[i], sentence2[i]) not in similar_set and (sentence2[i], sentence1[i]) not in similar_set:
                return False
        return True
# @lc code=end

