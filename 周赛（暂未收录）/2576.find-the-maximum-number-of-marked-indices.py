class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        mid = n // 2
        j = mid
        res = 0
        for i in range(0, mid):
            while j < n and nums[j] < nums[i] * 2:
                j += 1
            if j < n:
                res += 2
                j += 1
        return res