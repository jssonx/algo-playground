class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = [(num, i) for i, num in enumerate(nums)]
        num_idx.sort()
        left = 0
        right = len(num_idx) - 1
        while left < right:
            s = num_idx[left][0] + num_idx[right][0]
            if s == target:
                return [num_idx[left][1], num_idx[right][1]]
            elif s > target:
                right -= 1
            else:
                left += 1
