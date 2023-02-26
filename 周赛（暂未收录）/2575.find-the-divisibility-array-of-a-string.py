class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        if not word or m <= 0:
            return []
        res = []
        prev = 0
        for i in range(len(word)):
            cur = ord(word[i]) - ord('0')
            prev = (prev * 10 + cur) % m
            res.append(1 if prev == 0 else 0)
        return res