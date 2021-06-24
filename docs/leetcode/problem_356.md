# 思路推导

假设给定的坐标点，能构成左右对称，则必须满足以下两个条件：

1. 这些坐标点中，Y 轴坐标相同的点，其 X 轴坐标左右对称；
2. 每一对成左右对称的坐标点，其 X 轴的中点相同，换言之，其 X 轴坐标之和相同；

因此，不难推导出以下解题步骤：

1. 假设可以构成左右对称，则 X 轴最小的点，必然和 X 轴最大的点成左右对称。因此可以通过遍历坐标点找到`min(x)`和`max(x)`，从而计算得二者之和，即为中点坐标 * 2；
2. 对所有坐标点，按 Y 轴坐标进行分组。考虑到可能存在重复的坐标点，所以使用 Set 来存储；
3. 对相同 Y 坐标的点的 X 坐标，依次计算是否存在 X'，使得 X + X' = 第一步里计算得到的中点坐标 * 2；

# 参考代码

```python3 []
class Solution:
    def is_reflected(self, points: List[List[int]]) -> bool:
        minimum, maximum = 100000000, -100000000
        store = collections.defaultdict(set)
        for p in points:
            x, y = p[0], p[1]
            minimum = min(minimum, x)
            maximum = max(maximum, x)
            store[y].add(x)
        summary = minimum + maximum
        for x_set in store.values():
            for x in x_set:
                if summary - x not in x_set:
                    return False
        return True
```

```java []
public class Solution {
    public boolean isReflected(int[][] points) {
        Map<Integer, Set<Integer>> group = new HashMap<>();
        int min = 100000000, max = -100000000;
        for (int[] point : points) {
            int x = point[0], y = point[1];
            min = Math.min(min, x);
            max = Math.max(max, x);
            if (group.containsKey(y)) {
                group.get(y).add(x);
            } else {
                Set<Integer> set = new HashSet<>();
                set.add(x);
                group.put(y, set);
            }
        }
        int sum = min + max;
        for (Map.Entry<Integer, Set<Integer>> entry : group.entrySet()) {
            Set<Integer> xSet = entry.getValue();
            for (int x : xSet) {
                if (!xSet.contains(sum - x))
                    return false;
            }
        }
        return true;
    }
}
```
