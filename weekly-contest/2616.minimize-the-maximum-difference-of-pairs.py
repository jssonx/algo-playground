class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        key = functools.partial(self.max_pairs, sorted(nums))
        return bisect.bisect_left(range(max(nums)), p, key=key)

    def max_pairs(self, nums: list[int], max_diff: int) -> int:
        cnt_pairs = 0
        i = 1
        while i < len(nums):
            if nums[i] - nums[i - 1] <= max_diff:
                cnt_pairs += 1
                i += 2
            else:
                i += 1
        return cnt_pairs