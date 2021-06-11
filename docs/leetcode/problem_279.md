# 思路分析

题目：要把正整数 x 拆分成最少个不同正整数的平方和。

不妨假设有一个现成的函数`U = func(x)`，其中`x`表示原正整数，`U`表示拆解出来的最少个正整数的集合。进一步假设正整数`a ∈ U`，即`a`是集合`U`中的正整数。则必然有：

```
U - a = func(x - a^2)
```

换句话说，当集合`U`中元素的个数是 n 的话，则正整数`x - a^2` 所能拆解出的最少完全平方数之和的集合为`U`去掉`a`后的补集。这个结论可以用反证法推出来。

因此，通过上面的分析，我们得到了以下结论

```
func(x) = 1 + ∑(min(func(x - a^2))), a^2 <= x
```

要对给定的正整数求其最少完全平方数表达，需要枚举位于正整数之前的数的最少完全平方数表达。上面的表达式转换成代码，可以用 DFS，也可以 DP。

# DFS 解法

```python []
class Solution:
    def num_squares(self, n: int) -> int:
        @lru_cache(None)
        def dfs(k: int) -> int:
            ret = k  # 最差情况是由 k 个 1 组成
            limit = int(k ** 0.5)
            for i in range(limit, 0, -1):
                ret = min(ret, 1 + dfs(k - limit * limit))
            return ret

        return dfs(n)
```

代码中使用了记忆化，避免对已经出现过的`k`重复执行`dfs(k)`。

# DP 解法

根据思路分析中的结论，可以用数组`dp[i]`表示正整数`i`的最少个完全平方数表达。其状态转移方程为：

```
dp[i] = min(i, 1 + ∑(dp[i - a^2])), a^2 <= i
```

```java []
class Solution {
    public int numSquares(int n) {
        int[] dp = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            dp[i] = i;
            for (int j = 1; j * j <= i; j++) {
                dp[i] = Math.min(dp[i], dp[i - j * j] + 1);
            }
        }
        return dp[n];
    }
}
```

# 抽象成最短路径问题

继续结合第一部分思路解析，正整数`x`可以拆解出的最少完全平方数表达的集合为`U`，假设 `(a, b, c) ∈ U`，也就是假设`x`可以由最少 3 个完全平方数求和。

那么从 x 到 0，最少需要执行三次减法，x - a^2 - b ^2 - c^2 = 0。

那么这就转化成一棵树的最短路径问题：树根是给定的正整数`x`，叶节点为 0，中间的非叶节点为`x`减去完全平方数后的差值。找到根节点到叶节点的最短路径。

```
        12
      / |  \
     3  8  11
    /  /|  | \ \
   2  4 7  2  7 10
  /  /  |  |  |  |
 1  0   3  1  3  1
/
0
```

这是典型的广度优先遍历问题。

```python3 []
class Solution:
    def num_squares(self, n: int) -> int:
        ans = 0
        queue = [n]
        while queue:
            ans += 1
            size = len(queue)
            for i in range(size):
                vertex = queue.pop(0)
                limit = int(vertex ** 0.5)
                for j in range(limit, 0, -1):
                    rem = vertex - j * j  # 减去 j 平方后还剩下 rem
                    if rem == 0:
                        return ans  # 发现 0，表示已经找到最短路径
                    queue.append(rem)
        return ans
"""
