LC198
```python
# 0: 本轮我抢的最大收益
# 1: 本轮我不抢的最大收益
for k in range(1, n+1):
    dp[i][0] = dp[i-1][1] + nums[i]
    dp[i][1] = max(dp[i-1][0], dp[i-1][1])
res = max(dp[n][0], dp[n][1])
```
