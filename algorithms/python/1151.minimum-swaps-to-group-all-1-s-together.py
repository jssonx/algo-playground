#
# @lc app=leetcode id=1151 lang=python3
#
# [1151] Minimum Swaps to Group All 1's Together
#

# @lc code=start
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones_count = sum(data)
        if ones_count == 0 or ones_count == len(data):
            return 0

        window_size = ones_count
        ones_in_window = sum(data[:window_size])

        max_ones_in_window = ones_in_window
        for i in range(window_size, len(data)):
            ones_in_window += data[i] - data[i - window_size]
            max_ones_in_window = max(max_ones_in_window, ones_in_window)

        return window_size - max_ones_in_window
# @lc code=end

