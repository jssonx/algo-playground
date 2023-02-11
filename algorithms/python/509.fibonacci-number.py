#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        p, q = 0, 1
        for i in range(2, n + 1):
            p, q = q, p + q
        
        return q


        
# @lc code=end

