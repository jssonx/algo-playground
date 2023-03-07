#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ranges = []
        start = end = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                ranges.append(self.get_range(start, end))
                start = end = nums[i]

        ranges.append(self.get_range(start, end))
        return ranges

    def get_range(self, start, end):
        if start == end:
            return str(start)
        else:
            return str(start) + "->" + str(end)

        
# @lc code=end

