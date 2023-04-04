#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#
# https://leetcode.com/problems/student-attendance-record-i/description/
#
# algorithms
# Easy (48.18%)
# Likes:    547
# Dislikes: 30
# Total Accepted:    175.2K
# Total Submissions: 363.6K
# Testcase Example:  '"PPALLP"'
#
# You are given a string s representing an attendance record for a student
# where each character signifies whether the student was absent, late, or
# present on that day. The record only contains the following three
# characters:
# 
# 
# 'A': Absent.
# 'L': Late.
# 'P': Present.
# 
# 
# The student is eligible for an attendance award if they meet both of the
# following criteria:
# 
# 
# The student was absent ('A') for strictly fewer than 2 days total.
# The student was never late ('L') for 3 or more consecutive days.
# 
# 
# Return true if the student is eligible for an attendance award, or false
# otherwise.
# 
# 
# Example 1:
# 
# 
# Input: s = "PPALLP"
# Output: true
# Explanation: The student has fewer than 2 absences and was never late 3 or
# more consecutive days.
# 
# 
# Example 2:
# 
# 
# Input: s = "PPALLL"
# Output: false
# Explanation: The student was late 3 consecutive days in the last 3 days, so
# is not eligible for the award.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s[i] is either 'A', 'L', or 'P'.
# 
# 
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        if self.checkA(s) and self.checkL(s):
            return True
        else:
            return False
    
    def checkA(self, s: str) -> bool:
        nums = Counter(s)
        return nums['A'] < 2
    
    def checkL(self, s: str) -> bool:
        n = len(s)
        for i in range(n - 2):
            if s[i:i+3] == "LLL":
                return False
        return True
        
# @lc code=end

