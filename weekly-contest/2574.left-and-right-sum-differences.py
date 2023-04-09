class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        leftSum = [0] * n
        rightSum = [0] * n
        for i in range(1, n):
            leftSum[i] = leftSum[i-1] + nums[i-1]
        for i in range(n-2, -1, -1):
            rightSum[i] = rightSum[i+1] + nums[i+1]
        for i in range(n):
            ans.append(abs(leftSum[i] - rightSum[i]))
        return ans