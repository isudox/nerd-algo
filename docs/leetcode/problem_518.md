# 思路推导

对于任意硬币，可以选择使用，或者不使用：

- 选择使用当前硬币`coins[i]`，则后续需要凑成`amount-coins[i]`；
- 不使用当前硬币，则后续需要凑成`amount`；

因此，可以用最朴素的深度优先搜索，遍历每个硬币，枚举两种不同策略。

# 朴素 DFS

定义方法`dfs(i, j)`，其中参数`i`表示当前遍历到的硬币偏移量，`j`表示要凑成的硬币总和。则要求的结果就是`dfs(len(coins) - 1, amount)`

为了避免 DFS 重复计算，引入记忆法，即空间换时间，用字典/数组记录已经计算过的`dfs(i, j)`。

参考代码如下：

```python3 []
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def dfs(i: int, j: int) -> int:
            if i < 0:
                return 0
            if j == 0:
                return 1
            if memo[i][j] != -1:
                return memo[i][j]
            memo[i][j] = dfs(i - 1, j) + (dfs(i, j - coins[i]) if j >= coins[i] else 0)
            return memo[i][j]

        memo = [[-1] * (amount + 1) for _ in range(len(coins))]
        return dfs(len(coins) - 1, amount)
```

需要注意的是，如果当前硬币选，则下一步 DFS 仍然得从当前硬币继续枚举，而不是跳转到下一枚硬币。（因为题设是允许重复选同一硬币）

# DFS 转 DP

具备前后依赖关系的 DFS，往往是可以转化为 DP 解法。这道题就是典型案例。
从 DFS 的代码中容易看出，当前`dfs(i, j)`的结果，是和之后的`dfs(i - 1, j)`以及`dfs(i, j - coins[i]`紧密相关。其关联关系就是 DP 所需的状态转移方程。

```
dfs(i,  j) = dfs(i - 1, j)

if j >= coins[i]:
    dfs(i, j) += dfs(i, j - coins[i]
```

所以，不难将上面的 DFS 代码转换为 DP 代码，本质上就是把 DFS 中的`memo[]`数组替换成`dp[]`数组而已。参考如下：

```python3 []
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        for i in range(len(coins) + 1):
            dp[i][0] = 1
        for i in range(1, len(coins) + 1):
            for j in range(1, amount + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= coins[i - 1]:
                    dp[i][j] += dp[i][j - coins[i - 1]]
        return dp[-1][-1]
```

DP 代码微调了下`dp[i][j]`中坐标`i`的含义，`i`表示前`i`个硬币。

# DP 降维

进一步分析上面的 DP 代码，可以观察到，`dp[i][j]`只和两个之前的状态有关，即`dp[i - 1][j]`和`dp[i, j - coins[i]]`。
所以不需要记录二维数组`dp[][]`中所有的值，只需要记录一行，然后滚动更新其中的值即可。这就是二维降一维。

```python3 []
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * amount  # dp[i] 表示构成总和 i 的组合数
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]  # 当前硬币值 <= 所需目标和时，累加之前已知的组合数
```

降维后的 DP 代码，其实就是这样一个状态转移关系：

- `dp[i]` 表示凑成总和`i`的硬币组合总数；
- 依次枚举各个硬币，如果当前硬币`coin <= i`，则表示当前硬币可选，则累加上`dp[i - coin]`的组合数

同样的，一维的 DP 也可以转换成 DFS 代码。有兴趣的朋友可以试试。
