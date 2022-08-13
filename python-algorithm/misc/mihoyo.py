import collections
import functools
from typing import List

"""
有一颗包含 n 节点的树，节点编号为 1 到 n，1 为根
第 i 个节点有权重 a[i]。找到一条最长路径的大小，使得路径上节点的权重满足一大一小。
如果路径长度 = 1，则头尾两个节点权重不能相同。

输入
1. 整数 n，表示节点数。2 <= n <= 1e5
2. n - 1 个整数，第 i 个数表示节点 i+1 的父亲，父亲节点编号 < 儿子
3. n 个整数，第 i 个数表示第 i 个节点的权重。1 <= a[i] <= 1e9
 """


class Solution:
    def get_path(self, n: int, links: List[int], weights: List[int]) -> int:
        # @functools.lru_cache(None)
        def dfs(start: int, need_gt: bool) -> int:
            seen[start] = True
            w = weights[start - 1]
            ret = 0
            for nxt in graph[start]:
                if seen[nxt]:
                    continue
                if (need_gt and weights[nxt - 1] > w) or (not need_gt and weights[nxt - 1] < w):
                    ret = max(ret, dfs(nxt, not need_gt) + 1)
            seen[start] = False
            return ret

        graph = collections.defaultdict(list)
        for i, parent in enumerate(links):
            child = i + 2
            graph[parent].append(child)
            graph[child].append(parent)
        seen = [False] * (n + 1)
        ans = 0
        for i in range(1, n + 1):
            ans = max(ans, max(dfs(i, True), dfs(i, False)))
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.get_path(3, [1, 1], [1, 2, 3]))
    print(sol.get_path(5, [1, 2, 3, 4], [1, 2, 3, 4, 5]))
    print(sol.get_path(5, [1, 2, 3, 4], [1, 2, 1, 2, 1]))
    print(sol.get_path(10000, [1] * 9999, list(range(1, 10001))))
