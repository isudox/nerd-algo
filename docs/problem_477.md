# 算法思路

本题对比 #461 题，区别在于，本题是要求所有数两两之间的汉明距离的总和。如果直接套用 #461 的解法，相当于是计算 N^2 次 #461 题，时间复杂度过高。

换个角度，从本质出发。什么是汉明距离，就是两个二进制数，数字不同的位的个数。

因此可以考虑逐位计算汉明距离。

- 假设当前二进制数第 i 位的数字为 1，则增加的汉明距离为之前所统计的 0 的个数；
- 反之，假设当前数位为 0，则增加的汉明距离为之前所统计的 1 的个数；

结合题设给定的`nums[i] <= 10^9`，可知所有二进制数的最长位数为 30。所以可以从从 0 位开始逐个计算到最高位。

参考代码如下，其中`counter[]`记录当前数位上，已遍历数字的 0 和 1 的个数：

```python3 []
class Solution:
    def total_hamming_distance(self, nums: List[int]) -> int:
        ans = 0
        for i in range(30):
            counter = [0, 0]
            for num in nums:
                bit = (num >> i) & 1
                counter[bit] += 1
                ans += counter[1 - bit]
        return ans
```

另一种思路是，直接计算每个二进制数位上，不同数字的组合数，即该数位的汉明距离。比如第 i 位上，1 的个数是 x，0 的个数是 y，则汉明距离就是 x * y。

```python3 []
class Solution:
    def total_hamming_distance(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(30):
            cnt = 0
            for num in nums:
                if (num >> i) & 1 == 1:
                    cnt += 1
            ans += cnt * (n - cnt)
        return ans
```
