package com.leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * 56. Merge Intervals
 * https://leetcode.com/problems/merge-intervals/
 */
public class Problem56 {
    public int[][] merge(int[][] intervals) {
        if (intervals == null || intervals.length == 0) return intervals;
        Arrays.sort(intervals, (o1, o2) -> o1[0] - o2[0]);
        List<int[]> merged = new ArrayList<>();
        merged.add(intervals[0]);
        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] <= merged.get(merged.size() - 1)[1]) {
                merged.get(merged.size() - 1)[1] = Math.max(intervals[i][1], merged.get(merged.size() - 1)[1]);
            } else {
                merged.add(intervals[i]);
            }
        }
        int[][] ans = new int[merged.size()][2];
        return merged.toArray(ans);
    }
}
