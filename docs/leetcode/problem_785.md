# [785. Is Graph Bipartite] DFS 遍历分组节点

## 题目分析

从题目可知以下关键信息：

- 图可能非联通，即可能存在多个隔离的联通图；
- 对于联通图，可以从任意点出发，遍历所有点；
- 对于已经确定归属集合的点 A，与其相连的点必须归属到另一集合；

不难发现，要对图进行二分图校验，需要对每个点进行集合拆分。因此必然涉及遍历，而图的遍历，无非`DFS`和`BFS`。

 - 情况 1: 图只有一个联通图。那么从节点 0 开始遍历（作为起点，可以放置在任意集合，假定归属在集合 1），可以把节点 0 所在的联通图正确拆分到归属集合
 - 情况 2: 图不止一个联通图。那么需要对所有节点依次作为起点进行遍历，其中对于已经遍历过的节点，可以跳过。

在遍历过程中，如果发现节点 x 应该在集合 1，却出现在集合 2，那么可以断定该图不是二分图。

## 算法思路

结合图的遍历，我们可以采用`DFS`或者`BFS`。下面以`DFS`为例，提供算法思路的参考。
首先需要建立一个数组`seen`，表示节点是否已经被遍历过，已遍历过的节点无需再次遍历。其次需要建立数组`groups`，记录节点被划分的归属集合。考虑到节省空间，我们可以把这两个数组合并，用不同数字表示——

1. 是否已被遍历
2. 遍历后，被划分的集合

可以用 0 表示未遍历，1 表示被划分到集合 A，-1 表示被划分到另一集合 B。

```python3
class Solution:
    def is_bipartite(self, graph: List[List[int]]) -> bool:
        def dfs(x: int, flag: int) -> bool:
            groups[x] = flag
            for y in graph[x]:
                if groups[y] == flag:
                    return False
                if groups[y] == 0:
                    if not dfs(y, -flag):
                        return False
            return True

        n = len(graph)
        groups = [0] * n  # 0 ungrouped, 1: group A, -1: group B
        for i in range(n):
            if groups[i] == 0:
                if not dfs(i, 1):  # 如果某节点未遍历，说明它是没被遍历过的联通图的节点，直接放置在集合 A
                    return False
        return True
```

![截屏2022-04-29 下午3.55.56.png](https://pic.leetcode-cn.com/1651218973-kylziO-%E6%88%AA%E5%B1%8F2022-04-29%20%E4%B8%8B%E5%8D%883.55.56.png)