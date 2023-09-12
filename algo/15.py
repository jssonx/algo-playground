class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        prev = float("inf")
        for i in range(n-2):
            num1 = nums[i]
            if num1 == prev:
                continue
            if num1 + nums[i+1] + nums[i+2] > 0:
                break
            if num1 + nums[-1] + nums[-2] < 0:
                continue
            left, right = i+1, n-1
            while left < right:
                ssum = num1 + nums[left] + nums[right]
                if ssum == 0:
                    res.append([num1, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif ssum > 0:
                    right -= 1
                elif ssum < 0:
                    left += 1
            prev = num1
        return res
