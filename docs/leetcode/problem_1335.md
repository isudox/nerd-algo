# 状态迁移 + 预计算优化

## 题目分析

如果把这道情景题抽象出来，就是将数组`jobDifficulty`拆分成`d`个非空子数组，使得所有子数组的最大数的总和最小。
那么首先可以排除一个情况，就是数组元素个数小于`d`时，必然无法拆分。返回 -1。

再从一般性考虑，假设对数组前 x 个元素拆分到 y 个非空子数组，从而使得总难度最小。该 y 个子数组，可以由前面的 y-1 个子数组，加后面的 1 个子数组拼成。如下所示——

```
[ 第 1 子数组 ]、[第 2 子数组]、[第 3 子数组]…… [第 y-1 子数组] ｜ [第 y 子数组]
```

如果前面 y-1 个子数组所有元素的个数为 m，则第 y 个子数组内元素个数为 x-m 个。而数组前 m 个元素拆分到 y-1 个子数组，就是状态方程的前一状态。
推导到这，对动态规划有所了解的人已经能看出明显的状态迁移迹象了。

## 算法

这是典型的动态规划题目，其状态迁移方程为：

```
dp[x][y] = dp[i][y-1] + max_difficulty_between[i+1][x], i ∈ [0, x)
```

为了避免重复计算数组某个区间的最大难度，我们可以预先计算并存储在二维数组中，计为`maxDifficulty`。`maxDifficulty[a][b]`表示第 a 个元素到第 b 个元素的最大值。

用代码来呈现上述状态方程，参考如下：

```java
dp[x][y] = Integer.MAX_VALUE;
for (int i = 0; i < x; i++) {
    dp[x][y] = Math.min(dp[x][y], dp[i][j - 1] + maxDifficulty[i + 1][x]);
    // 其中，maxDifficulty[a][b] 表示 jobDifficulty[a] 到 jobDifficulty[b] 的最大难度
}
```

## 参考代码

```java
public class Problem1335 {
    public int minDifficulty(int[] jobDifficulty, int d) {
        int n = jobDifficulty.length;
        if (n < d) {
            return -1;
        }
        int[][] maxDifficulty = new int[n][n]; // 预计算从 第 i 到第 j 项工作的最大难度
        for (int i = 0; i < n; i++) {
            maxDifficulty[i][i] = jobDifficulty[i];
            for (int j = i + 1; j < n; j++) {
                maxDifficulty[i][j] = Math.max(maxDifficulty[i][j - 1], jobDifficulty[j]);
            }
        }
        int[][] dp = new int[n][d + 1]; // dp[i][j] 表示截止到第 i 项工作，耗时 j 天的总难度
        for (int i = 0; i < n; i++) {
            Arrays.fill(dp[i], -1);
        }
        for (int i = 0; i < n; i++) {
            dp[i][1] = maxDifficulty[0][i];
            for (int j = 2; j <= Math.min(d, i + 1); j++) {
                dp[i][j] = Integer.MAX_VALUE;
                for (int k = 0; k < i; k++) {
                    if (dp[k][j - 1] > -1) {
                        // dp[i][j] = dp[k][j - 1] + max_difficulty[k+1][j]
                        dp[i][j] = Math.min(dp[i][j], dp[k][j - 1] + maxDifficulty[k + 1][i]);
                    }
                }
            }
        }
        return dp[n - 1][d];
    }
}
```
