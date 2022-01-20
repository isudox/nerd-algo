# [219] 利用哈希表记录出现过数的位置

## 思路分析

依题意，当存在 `i` + `k` <= `j`，使得 `nums[i]` = `nums[j]` 时，返回 `true`，否则 `false`。

因此，必然需要对给定数组做遍历，对当前遍历到的数：

- 如果在之前的遍历中已经出现过，则比较当前索引位和前一次出现的索引位的距离
    - 如果索引位的距离 <= k，是则返回 true，结束；
    - 如果索引位的距离 > k，则更新哈希表中该数出现的位置；
- 如果在之前的遍历中没有出现过，则记录该数出现的位置；

## 参考代码

```python3 []
def contains_nearby_duplicate(nums: List[int], k: int) -> bool:
    store = collections.defaultdict(int)
    for i, num in enumerate(nums):
        if num in store and i - store[num] <= k:
            return True
        store[num] = i
    return False
```
