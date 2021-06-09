# 算法思路

## 分析过程
对数组中所有元素，分别取正，或者取反，使得最终相加为目标和。实际上是要枚举所有可能的组合，如果用暴力破解，则要推演`2^len(nums)`个组合，复杂度就比较高了。

对于数组中任意一个数，采取的策略只有两种：1）取正，即前置`+`号；2）取反，前置`-`号。而当前的操作会影响数组后续元素所要求的目标和：

- 对`nums[i]`取正，则后面的元素和则为`target - nums[i]`；
- 对`nums[i]`取反，则后面的元素和则为`target + nums[i]`；

因此不难发现，这里面隐藏了递归的逻辑，很容易就写出递归的算法，但这样不行，因为没有改变计算量。

## DFS

进一步思考，对`nums[i]`选择处理策略后，紧接着对`nums[i+1]`进行处理，以此类推，这就是 DFS 的过程。而 DFS 的优化，有两个方向：

1. 记忆法，即记录执行过的计算结果，下次 DFS 再进来，直接返回，避免重复计算；
2. 剪枝法，即通过逻辑判断当前 DFS 是否有必要进行，无必要则结束；

记忆法对于本题，是简单可行的：只需要缓存记录下各个数组偏移量和不同目标和，所计算得到的结果值；
而剪枝法不适用本题，因为 DFS 到某个数组元素时，并不能确定后续的元素是否能够构成目标和。

示例代码用 Python 语法糖来做 DFS 记忆，比较简单。

```python3 []
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(i: int, t: int) -> int:
            if i == len(nums):
                return 1 if t == 0 else 0
            return dfs(i + 1, t - nums[i]) + dfs(i + 1, t + nums[i])

        return dfs(0, target)
```

## DP

算法题刷的多的朋友，可能看到题目就意识的想到这是「背包问题」，背包问题的经典解法就是动态规划。

如果一上手想不到状态转移方程，不妨从直观的解法入手，慢慢寻找到状态转移关系。比如这道题就是典型的记忆法 DFS -> DP 的算法案例。

在 DFS 的解法中，实际是用了一个数组`memo[i][t]`记录数组第`i`个元素开始到最后一个元素，目标和为`t`的表达式数量。（上面示例代码中用的是`functools.lru_cache`，只是语法糖而已）
其中，`memo[i][t]`和它右边的元素有关，其关联关系为：

```plaintext
memo[i][t] = memo[i + 1][t - nums[i]] + memo[i + 1][t + nums[i]]
```

这不就是动态规划的状态转移方程嘛！本题所需的`dp`就是上面的`memo[]`数组。

因此，我们只需要从右往左推导出`dp`数组，`dp[i][j]`表示从数组元素`nums[i]`开始，目标和为`j`的表达式数量。需要注意的是，避免坐标`j`为负数，需要加上的偏移量。
偏移量设置多少合适，考虑到题设中数组元素非负，因此可能的元素和区间为`[-sum(nums), sum(nums]`，因此偏移量 offset 设置为`sum(nums)`即可。

DP 的示例代码如下，因为涉及的边界条件会比较多，容易写错，总体推荐用 DFS 来解，思路清晰的多。

```python3 []
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        offset = sum(nums)
        if target > offset:
            return 0
        limit = 2 * offset + 1
        dp = [[0] * limit for _ in range(len(nums))]
        if nums[-1] == 0:
            dp[-1][offset - nums[-1]] = 2
        else:
            dp[-1][offset - nums[-1]] = 1
            dp[-1][offset + nums[-1]] = 1
        for i in range(len(nums) - 2, -1, -1):
            for j in range(-offset, offset + 1):
                if offset + j >= 0:
                    dp[i][offset + j] += dp[i + 1][offset + j - nums[i]]
                if offset + j + nums[i] < limit:
                    dp[i][offset + j] += dp[i + 1][offset + j + nums[i]]
        return dp[0][offset + target]]
```
