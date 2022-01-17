# 思路分析

首先明确一个先决条件——

> 假设 Alex 选择座位`i`，则该位置`i`必然位于距离最大的两个已经有人坐的座位`x`和`y`之间。产生的距离为 (y-x) / 2

但这个条件里，还隐藏了一种特殊情况，因为两个边界位置`0`和`len(seats)-1`，与其相距最近的有人坐的座位中间，也可能产生题目所需的答案。

因此，解题的思路就是要比较三种情形中距离的大小，选择最大的距离即可：

1. 位置`0` 和第一个有人坐的座位之间的距离；
2. 位置`len(seats)-1`和最后一个有人坐的座位之间距离；
3. 相距最大的两个有人坐的座位之间的距离除以 2；

# 参考代码

```java
class Solution {
    public int maxDistToClosest(int[] seats) {
        int maxInterval = 1;
        int prePos = -1;
        int ans = 1;
        for (int i = 0; i < seats.length; i++) {
            if (seats[i] == 1) {
                if (prePos == -1) {
                    // find first `1`
                    ans = i;
                }
                int curInterval = i - prePos;
                if (curInterval > maxInterval) {
                    maxInterval = curInterval;
                }
                prePos = i;
            }
        }
        ans = Math.max(ans, seats.length - 1 - prePos);
        return Math.max(ans, maxInterval / 2);
    }
}
```

- 时间复杂度: `O(N)`
- 空间复杂度: `O(1)`