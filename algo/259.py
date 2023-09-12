class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                ssum = nums[i] + nums[left] + nums[right]
                if ssum < target:
                    count += (right - left)
                    left += 1
                else:
                    right -= 1
        return count
