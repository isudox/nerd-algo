package com.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 1046. Last Stone Weight
 * https://leetcode.com/problems/last-stone-weight/
 * 输入：[2,7,4,1,8,1]
 * 输出：1
 * 解释：
 * 先选出 7 和 8，得到 1，所以数组转换为 [2,4,1,1,1]，
 * 再选出 2 和 4，得到 2，所以数组转换为 [2,1,1,1]，
 * 接着是 2 和 1，得到 1，所以数组转换为 [1,1,1]，
 * 最后选出 1 和 1，得到 0，最终数组转换为 [1]，这就是最后剩下那块石头的重量。
 */
public class Problem1046 {
    public int lastStoneWeight(int[] stones) {
        Arrays.sort(stones);
        List<Integer> list = new ArrayList<>();
        for (int s : stones) {
            list.add(s);
        }
        while (list.size() >= 2) {
            int s1 = list.remove(list.size() - 1);
            int s2 = list.remove(list.size() - 1);
            if (s1 != s2) {
                int s3 = s1 - s2;
                int idx = search(list, s3);
                list.add(idx, s3);
            }
        }
        return list.size() == 0 ? 0 : list.get(0);
    }

    private int search(List<Integer> list, int num) {
        int lo = 0, hi = list.size() - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (list.get(mid) == num) {
                return mid;
            }
            if (list.get(mid) < num) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return lo;
    }
}
