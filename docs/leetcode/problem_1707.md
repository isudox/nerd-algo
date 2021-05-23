# 算法思路

> 这题我并没有独立算出来，而是在参考了题目下面给出的 4 条提示才想到之前做过类似的题目，套用了下思路。

要使得 A ^ B 的值最大，则 A 和 B 二进制数越高位的数不同，则异或后的结果相应越大。由于题设中限定了所有数字都在区间 [0, 10^9]，因此所有数的二进制数都可以用 31 位长度表示。

先从最小问题出发，假设其中一个 query 为`x`和`m`，需要在`nums[]`数组中，找到所有`nums[j] <= m`，和`x`进行异或，找到最大的异或值。这里有两个信息可以捕获：

1. 需要到数组`nums[]`进行排序，方便找到所有符合条件的`nums[j]`；
2. 找到所有`nums[j]`后，如果逐一和`x`异或，可行，但速度太慢，因为对于有些数，根据其高位二进制数可以快速将其排除掉。

关键的第二步，怎么快速排除？既然要二进制的高位筛选，每次都要找和`x`对应位不同的数，那么不妨把所有二进制数从高位到底位，分别插入到字典树中，在字典树中寻找路径，最终得到的路径所代表的结果，就是所求的最大异或值。

另一个问题，各个`query`中的`m`大小不一，为了避免构造了一棵由`nums[j] <= m`的字典树后，重新再去构造`nums[j] <= m - n`（这里的 m - n 表示比 m 小的数）的字典树，需要提前把`queries[]`数组按`m`，即`query[1]`从小到大排序。这么做就是让之前每次的插入字典树动作，都能为后面的`query`动作做准备。

## 字典树

本题中的字典树，需要用到的只有字典树的插入，由于插入的是二进制数位上的 0 或 1，因此这棵字典树度 <= 2。可以按如下定义：

```python3
"""字典树定义
left 表示节点为 0
right 表示节点为 1
"""
class Trie:
    def __init__(self) -> None:
        self.left = None
        self.right = None
```

字典树的插入：

```python3
"""二进制数按数位，从高到低，插入字典树"""

def add(root: Trie, num: int):
    cur = root
    for k in range(30, -1, -1):
        bit = (num >> k) & 1  # 求二进制数第 k 位
        if bit == 0:
            if not cur.left:
                cur.left = Trie()
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = Trie()
                cur = cur.right
```

# 参考代码

```python3 []
class Solution:
    def maximize_xor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def add(num: int):
            cur = root
            for k in range(30, -1, -1):
                bit = (num >> k) & 1
                if bit == 0:
                    if not cur.left:
                        cur.left = Trie()
                    cur = cur.left
                else:
                    if not cur.right:
                        cur.right = Trie()
                    cur = cur.right

        def cal(num: int) -> int:
            if not root.left and not root.right:
                return -1
            cur = root
            ret = 0
            for k in range(30, -1, -1):
                bit = (num >> k) & 1
                if bit == 0:
                    if cur.right:
                        cur = cur.right
                        ret = (ret << 1) + 1
                    else:
                        cur = cur.left
                        ret = ret << 1
                else:
                    if cur.left:
                        cur = cur.left
                        ret = (ret << 1) + 1
                    else:
                        cur = cur.right
                        ret = ret << 1
            return ret

        nums.sort()
        ans = [0] * len(queries)
        for i, query in enumerate(queries):
            query.append(i)
        queries.sort(key=lambda x: x[1])
        root = Trie()
        j = 0
        for x, m, i in queries:
            while j < len(nums):
                if nums[j] <= m:
                    add(nums[j])
                    j += 1
                else:
                    break
            ans[i] = cal(x)
        return ans
```
