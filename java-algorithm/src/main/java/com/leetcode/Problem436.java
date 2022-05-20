package com.leetcode;

import java.util.*;

/**
 * 436. Find Right Interval
 * https://leetcode.com/problems/find-right-interval/
 */
public class Problem436 {
    public int[] findRightInterval(int[][] intervals) {
        int n = intervals.length;
        int[] ans = new int[n];
        Arrays.fill(ans, -1);
        TreeMap<Integer, Integer> treeMap = new TreeMap<>();
        for (int i = 0; i < n; i++) {
            treeMap.put(intervals[i][0], i);
        }
        List<Integer> list = new ArrayList<>(treeMap.keySet());
        for (int i = 0; i < n; i++) {
            int idx = find(list, intervals[i][1]);
            if (idx == -1) {
                ans[i] = -1;
            } else {
                ans[i] = treeMap.get(list.get(idx));
            }
        }
        return ans;
    }

    private int find(List<Integer> list, int target) {
        if (target > list.get(list.size() - 1)) {
            return -1;
        }
        int lo = 0, hi = list.size() - 1, mid;
        while (lo < hi) {
            mid = lo + (hi - lo) / 2;
            int ret = list.get(mid);
            if (ret == target) {
                return mid;
            }
            if (ret < target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}
