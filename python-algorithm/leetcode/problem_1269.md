# 解题思路

其实拿到这道题，应该能敏锐的嗅到「动态规划」的臭味。因为用走 n 步仍然在原点的走法，和 n - 1 步在什么位置是密切相关的。

从问题出发，要求走了 n 步后，仍然在原点的所有走法数量，先考虑 n-1 步。假设走了 n-1 步后，位置在 x 处，那么再走一步的话，只可能来到 x-1，x，x+1，如果要回到原点 0，意味着：

```
x - 1 = 0 || x = 0 || x + 1 == 0
```

因为存在边界，所以第 n-1 步只能走到 0 或 1。继续往上推，要使得第 n-1 步走到 0 或者 1，表明第 n-2 步就一定要走到 0，1，2。逐层反推，可得动态规划的状态转移方程为：

```
dp[i][j] = dp[i-1][j] + dp[i-1][j-1] + dp[i-1][j+1]    i,j 均不越界
```

其中，`dp[i][j]` 中，表示走了 i 步位于 arr[j] 位置上的走法数量（按题意，对`1e9+7`取模）。`dp[0][0]` = 1

题目要求的结果为`dp[steps][0]`。

# 算法代码

```java []
class Solution {
    public int numWays(int steps, int arrLen) {
        int base = (int) (1e9 + 7);
        int[] dp = new int[]{1};
        for (int i = 1; i <= steps; i++) {
            int[] nextDp = new int[i + 1];
            for (int j = 0; j < Math.min(i + 1, arrLen); j++) {
                int cur = 0;
                if (j <= i - 1) cur = (cur + dp[j]) % base;
                if (j - 1 >= 0) cur = (cur + dp[j - 1]) % base;
                if (j + 1 <= Math.min(i - 1, arrLen - 1)) cur = (cur + dp[j + 1]) % base;
                if (i == steps)
                    return cur;
                nextDp[j] = cur;
            }
            dp = nextDp;
        }
        return dp[0];
    }
}

```

```python3 []
class Solution:
    def num_ways(self, steps: int, arr_len: int) -> int:
        base = 1000000007
        dp, next_dp = [1], []
        for i in range(1, steps + 1):
            for j in range(min(i + 1, arr_len)):
                cur = 0
                if j <= i - 1:
                    cur = dp[j]
                if j - 1 >= 0:
                    cur = (cur + dp[j - 1]) % base
                if j + 1 <= i - 1 and j + 1 <= arr_len - 1:
                    cur = (cur + dp[j + 1]) % base
                if i == steps:
                    return cur
                next_dp.append(cur)
            dp = next_dp
            next_dp = []
        return dp[0]
```
