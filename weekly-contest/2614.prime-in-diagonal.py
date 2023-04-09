class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        res = 0
        # One diagonal
        n = len(nums)
        for i in range(n):
            cur = nums[i][i]
            if self.isPrime(cur) == True:
                res = max(res, cur)
        # Another diagonal: nums[i][nums.length - i - 1]= val
        for i in range(n):
            cur = nums[i][n - i - 1]
            if self.isPrime(cur) == True:
                res = max(res, cur)
        return res
    
    def isPrime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True