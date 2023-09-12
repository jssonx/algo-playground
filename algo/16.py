class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            start, end = i+1, len(nums)-1
            while start < end:
                _sum = nums[start] + nums[end] + nums[i]
                if abs(target - _sum) < abs(target - ans):
                    ans = _sum
                if _sum > target:
                    end -= 1
                elif _sum < target:
                    start += 1
                else:
                    return ans
        return ans
