# 算法思路

本题的题意比较好分析，用数学描述就是：

对数字 0 ~ len(group)-1 任意取数进行组合，所选数的组合，能使`sum(group[i]) <= n`且`sum(profit(i)) >= minProfit`，其中，`i`为组合中的数字。

因此，只要对数组`[0, 1, 2, ... len(group) - 1]`做枚举，一定可以求出所有可能组合。这就是最朴素的 DFS 解法。但是这样做，时间复杂度太高，因为总共有`2^len(group)`种枚举。

那对 DFS 的优化有哪些手段？我之前的题解中提到过，可以从下面两方面着手：

1. 剪枝法。通过逻辑条件，判断出当前 DFS 不可能得到想要的结果，提前结束。
2. 记忆法。即已经执行过的 DFS，不要重复计算，直接返回先前的计算结果。（空间换时间）

## 思路推敲一：剪枝优化

那能剪枝吗？

可以。因为题目中对工人数量做了限制，因此当 DFS 过程中，发现工人不够用了，就无需继续 DFS。
那怎么判断工人是否够用，我又不知道后面的工作，分别需要多少工人。这很好办，只需要对工人进行排序，就是抽象出「所需工人数-对应工作」的对儿，然后按所需工人数排序。当 DFS 在某一项工作，发现剩余工人不足以完成此项工作，那么后续的工作必然也无法完成，提前结束 DFS。

所以我们需要对输入参数进行加工，如果是 Python 的话，可以直接用`tuple`表示，即`(group[i], profit[i])`。

## 思路推敲二：记忆优化

那能通过记忆法，空间换时间，规避重复计算吗？

也是可以的。因为当 DFS 到第`i`项工作时，已经知道剩余工人数，已经剩余所需的 profit 数，如果后面的 DFS 再一次进入该条件，可以直接返回上次计算的结果。
也就是说，问题变成，从第`i`项工作开始，剩余有 x 个工人，需要 y 的收益，问有多少种组合。非常直观的记忆法。

## 参考代码

下面是用 DFS + 记忆 + 剪枝的优化

```python3 []
class Solution:
    def profitable_schemes(self, n: int, min_profit: int, group: List[int], profit: List[int]) -> int:
        @lru_cache(None)
        def dfs(i: int, left_workers: int, left_profit: int) -> int:
            if i == len(group):
                return 1 if left_profit == 0 else 0
            ret = 0
            if left_profit == 0:
                if left_workers >= pairs[i][0]:
                    ret += dfs(i + 1, left_workers - pairs[i][0], 0)
                ret += dfs(i + 1, left_workers, 0)
            elif left_workers >= pairs[i][0]:
                ret += dfs(i + 1, left_workers - pairs[i][0],
                           max(0, left_profit - pairs[i][1]))
                ret += dfs(i + 1, left_workers, left_profit)
            return ret % 1000000007

        pairs = list()
        for i in range(len(group)):
            pairs.append((group[i], profit[i]))  # 排序，以便剪枝
        pairs.sort(key=lambda x: x[0])
        return dfs(0, n, min_profit)
```
