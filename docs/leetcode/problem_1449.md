# 思路分析

对于给定的成本数组`cost[]`，每次取数，都可以从中任意取，只要没有超出总目标成本。那么如何才能凑出最大的数？最直观的想法是，枚举所有可能。但这么处理，复杂度非常高。

假设在枚举过程中，当前选择的数是`x`，即本次所花费的成本是`cost[x-1]`。那么剩余可用的成本为`target-cost[x-1]`。之后继续从`cost[]`数组中选择，如果要使最终构造的数字尽可能大，则必须要让剩余成本为`target-cost[x-1]`所凑成的数字尽可能大。那么问题就变成了成本为`target-cost[x-1]`时能凑出的最大数。

分析到这里，应该不难想到这可以用 DFS 和 DP 来做，二者本质相同，只是写法上的区别：

- DFS 思路：遍历`cost[]`数组，如果所遍历的元素可选（即花费成本 <= 当前剩余成本），则继续 DFS。为了避免对相同的剩余成本的重复计算，需要引入**记忆法**。
- DP 思路：定义`dp[]`数组，`dp[i]`表示目标成本为`i`时，所构造的最大数字。

# DFS 解

DFS 的解法相对更直观。注意数字型字符串的大小比较。

另外需要考虑，DFS 过程中，可能存在无法全部用掉剩余成本的情况，即无法凑出数字。这时可以返回`0`，因为题设中已经表明，`0`是不会凑出来的。

这里偷懒，用 Python 的`lru_cache`来做记忆法，参考如下——

```python3 []
class Solution:
    def largest_number(self, cost: List[int], target: int) -> str:
        def compare(a: str, b: str) -> bool:
            return a > b if len(a) == len(b) else len(a) > len(b)

        @lru_cache(None)
        def dfs(x: int) -> str:
            if x == 0:
                return ''
            res = '0'
            for i in range(len(cost)):
                if cost[i] <= x:
                    ret = dfs(x - cost[i])
                    if ret != '0':
                        ret = str(i + 1) + ret
                        if compare(ret, res):
                            res = ret
            return res

        return dfs(target)
```

# DP 解

DP 的解法，实质上是脱胎于 DFS 解法中的记忆数组。换句话说，DP 解法中的`dp[i]`，本质上就是 DFS 解法中的`dfs(i)`方法。细心揣摩下，这种转换是通用的。

```python3 []
class Solution:
    def largest_number(self, cost: List[int], target: int) -> str:
        def gt(a: str, b: str) -> bool:
            return a > b if len(a) == len(b) else len(a) > len(b)

        dp = [''] * (target + 1)
        for i in range(1, target + 1):
            dp[i] = '0'
            for j in range(9):
                if cost[j] <= i:
                    ret = dp[i - cost[j]]
                    if ret != '0':
                        ret = str(j + 1) + ret
                        if gt(ret, dp[i]):
                            dp[i] = ret
        return dp[target]
```

> 官方解法思路很漂亮，把复杂问题拆解为两个小问题：
> 1）DP 解出最大数字的位数；
> 2）利用 DP 数组，反推最能选出的最大数
> 我个人觉得官方解法的代码写出来并不好理解，不如 DFS 和上面的 DP 直观