
# A = {x | x <= 6}
# B = {x | x <= 2}
# C = {x | 3 <= x <= 6}
# C = A - B
class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()
        return self.less_equals(nums, upper) - self.less_equals(nums, lower - 1)
    
    def less_equals(self, nums: list[int], upper: int) -> int:
        count = 0
        right = len(nums) - 1

        for left in range(len(nums)):
            while right >= 0 and nums[left] + nums[right] > upper:
                right -= 1
            count += max(right - left, 0)

        return count