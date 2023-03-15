#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#
# https://leetcode.com/problems/maximum-swap/description/
#
# algorithms
# Medium (47.90%)
# Likes:    2942
# Dislikes: 165
# Total Accepted:    192.4K
# Total Submissions: 401.7K
# Testcase Example:  '2736'
#
# You are given an integer num. You can swap two digits at most once to get the
# maximum valued number.
# 
# Return the maximum valued number you can get.
# 
# 
# Example 1:
# 
# 
# Input: num = 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# 
# 
# Example 2:
# 
# 
# Input: num = 9973
# Output: 9973
# Explanation: No swap.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= num <= 10^8
# 
# 
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(str(num))
        n = len(num_list)
        last_occurrence = [-1] * 10
        
        for i in range(n):
            last_occurrence[int(num_list[i])] = i
        
        for i in range(n):
            digit = int(num_list[i])
            for j in range(9, digit, -1):
                if last_occurrence[j] > i:
                    num_list[i], num_list[last_occurrence[j]] = num_list[last_occurrence[j]], num_list[i]
                    return int(''.join(num_list))
        
        return int(''.join(num_list))

# @lc code=end

