# DFS -> DFS 记忆法优化 -> DP 状态转移

## 算法思路

先分析满足什么条件，两条线不相交。假设其中一条连线所连接的两个点分别是`nums1[i]`和`nums2[j]`，则另一条线所连接的两个点必须在 i 和 j 之后。这是满足不相交的充要条件。

### 思路一：贪心 + DFS

既然要使不相交的连线最多，则`nums1`中的点，要尽可能连接`nums2`数组中符合条件的最靠左的点。这是「贪心」的部分。

另一部分，当`nums1[i]`和可选的最左的`nums2[j]`相连后，可能因为`nums1[i]`后面的点无法再连接`nums2[j]`之前的点，导致不是最佳连法，因此，还要考虑放弃该连法。
因此，对于任意一组可能的连线，都要尝试连接，不连接，这两种路径，这是明显的 DFS 特征。

所以，方案一就是贪心的选择`nums2`数组最靠左的可选数字，DFS 的执行连线，不连线两种策略，最终得到最多的连线数。

注，可以提前遍历两个数组，将可能的连线全部存在字典中。

```python3 []
class Solution:
    def max_uncrossed_lines(self, nums1: List[int], nums2: List[int]) -> int:
        """DFS, Time Limit Exceeded"""
        def dfs(x: int, y: int) -> int:
            if x == len(nums1) or y == len(nums2):
                return 0
            ret = dfs(x + 1, y)
            for pos in lines[x]:
                if pos >= y:
                    ret = max(ret, dfs(x + 1, pos + 1) + 1)
                    break
            return ret

        lines = [[] for _ in range(len(nums1))]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    lines[i].append(j)
        return dfs(0, 0)
```

这个算法代码运行超时，显然是因为整个 DFS 过程中，对任意一对入参`(x, y)`都重复计算了。
所以这就可以考虑采用记忆法，优化 DFS 代码，即记录已经执行过的`dfs(x, y)`的值，当下一次再进入时，直接返回结果。

### 思路二：DFS + 记忆

用一个二位数字`memo[][]` 记录 DFS 每个路径节点的值。其中`memo[i][j]`表示从`nums1[i]`向右，`nums2[j]`向右，可连接的最多的不相交连线数。
`memo[][]`全部初始化为 -1，以区别 0。

```python3 []
class Solution:
    def max_uncrossed_lines(self, nums1: List[int], nums2: List[int]) -> int:
        """DFS + Memo"""
        def dfs(x: int, y: int) -> int:
            if x == len(nums1) or y == len(nums2):
                return 0
            if memo[x][y] != -1:
                return memo[x][y]
            ret = dfs(x + 1, y)
            for pos in lines[x]:
                if pos >= y:
                    ret = max(ret, dfs(x + 1, pos + 1) + 1)
                    break
            memo[x][y] = ret
            return ret

        lines = [[] for _ in range(len(nums1))]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    lines[i].append(j)
        memo = [[-1] * len(nums2) for _ in range(len(nums1))]
        return dfs(0, 0)
```

### 思路三：DP

通常，DFS + 记忆法，是可以转换为动态规划的。
从上面第二个解法中，不难发现，`memo[i][j]`和`memo[i+1][j+1]`，`memo[i+1][j]`相关。这里存在明显的状态转移关系。
在思路二中，`memo[i][j]`被定义为从`nums1[i]`起向右找，从`nums2[j]`起向右找，能连接的最多的不相交线数量。即：

- 当`nums1[i] == nums2[j]`时，`memo[i][j]`的一种可能值为`memo[i+1][j+1] + 1`，即在`memo[i+1][j+1]`基础上，连接`nums1[i]`和`nums2[j]`；
- 另外，也可以选择不连接`nums1[i]`和`nums2[j]`（另，如果两数不相等，显然也不能连接），则`memo[i][j]`的可能值为`memo[i+1][j]`，`memo[i][j+1]`;

上述状态转移关系是从右向左反着递推，不太好理解，可以翻转下。把`memo[i][j]`的定义调整为：从`nums1[0]`到`nums1[i]`，和`nums2[0]`到`nums2[j]`，最多的不相交连线数。
这就有了下面的动态规划解法。

```python3 []
class Solution:
    def max_uncrossed_lines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * len(nums2) for _ in range(len(nums1))]
        dp[0][0] = 1 if nums1[0] == nums2[0] else 0
        for i in range(1, len(nums1)):
            dp[i][0] = 1 if nums1[i] == nums2[0] else dp[i - 1][0]
        for j in range(1, len(nums2)):
            dp[0][j] = 1 if nums2[j] == nums1[0] else dp[0][j - 1]
        for i in range(1, len(nums1)):
            for j in range(1, len(nums2)):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if nums1[i] == nums2[j]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
        return dp[-1][-1]
```
