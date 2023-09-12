class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        num_idx = sorted((num, idx) for idx, num in enumerate(nums))
        l = 0
        r = len(nums) - 1
        cnt = 0
        while l < r:
            if num_idx[l][0] + num_idx[r][0] < target:
                cnt += (r - l)
                l += 1
            else:
                r -= 1
        return cnt