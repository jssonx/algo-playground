class Solution:
    def widestPairOfIndices(self, nums1, nums2):
        arr = []
        n = len(nums1)
        for i in range(n):
            arr.append(nums1[i] - nums2[i])
        pre_map = {} # presum -> idx
        pre_map[0] = -1
        
        pre_sum = 0
        res = 0
        for i in range(n):
            pre_sum += arr[i]
            if (pre_sum in pre_map):
                res = max(res, i - pre_map[pre_sum])
            else:
                pre_map[pre_sum] = i
        return res