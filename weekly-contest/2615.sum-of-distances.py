class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        dic = {}
        n = len(nums)
        res = [0] * n
        for i in range(n):
            index = nums[i]
            value = i
            if index not in dic:
                dic[index] = []
            dic[index].append(value)
    
        for key, value in dic.items():
                m = len(value)
                distance_sum = [0] * m
                distance_sum[0] = sum(abs(value[0] - x) for x in value)
                for i in range(1, m):
                    diff = value[i] - value[i-1]
                    distance_sum[i] = distance_sum[i - 1] + i * diff - (m - i) * diff
                for i in range(m):
                    res[value[i]] = distance_sum[i]
        return res