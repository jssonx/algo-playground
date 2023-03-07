#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[1] * (i+1) for i in range(rowIndex+1)]
        for i in range(2, rowIndex+1):
            for j in range(1, i):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        return triangle[rowIndex]
# @lc code=end

# class Solution:
#     def getRow(self, rowIndex: int) -> List[int]:
#         row = [1] * (rowIndex + 1)
#         print(row)
#         for i in range(1, rowIndex):
#             for j in range(i, 0, -1):
#                 row[j] += row[j-1]
#             print(row)
#         return row