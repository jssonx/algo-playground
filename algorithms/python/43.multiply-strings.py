#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        res = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1, p2 = i + j, i + j + 1
                sum = mul + res[p2]
                res[p2] = sum % 10
                res[p1] += sum // 10

        i = 0
        while i < len(res) and res[i] == 0:
            i += 1
        str_lst = [str(x) for x in res[i:]]
        return '0' if not str_lst else ''.join(str_lst)

# @lc code=end

