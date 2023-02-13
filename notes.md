# Notes

## DP问题
每一轮的状态都是一样的。我们要找到当前轮的状态和上一轮的状态之间的关系。（提示：想想买卖股票问题）

## 残酷DP勘误
冷冻期买卖股票
LC376 wiggle
276应该是265

## 198. House Robber
LC198
```python
# 0: 本轮我抢的最大收益
# 1: 本轮我不抢的最大收益
for k in range(1, n+1):
    dp[i][0] = dp[i-1][1] + nums[i]
    dp[i][1] = max(dp[i-1][0], dp[i-1][1])
res = max(dp[n][0], dp[n][1])
```
